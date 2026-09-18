from __future__ import annotations

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.osm_common.loader import load_catalog
from tools.osm_query.context_export import build_agent_context, dumps_agent_context
from tools.osm_query.queries import query_compliance, query_gaps, query_providers
from tools.tests.support import provider, service, stack, write_catalog


class GapTests(unittest.TestCase):
    def test_missing_accountable_and_critical_rto(self) -> None:
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack()],
                providers=[provider()],
                services=[
                    service(
                        "compute.virtual-machines",
                        name="Virtual Machines",
                        accountable=None,
                        offerings=[
                            {
                                "id": "compute.virtual-machines.aws",
                                "name": "EC2",
                                "providers": ["aws"],
                            }
                        ],
                    )
                ],
                posture=[
                    {
                        "service_id": "compute.virtual-machines",
                        "operational_criticality": "critical",
                        "offering_posture": [
                            {
                                "offering_id": "compute.virtual-machines.aws",
                                "rto": None,
                                "rpo": None,
                            }
                        ],
                    }
                ],
            )
            catalog = load_catalog(root)
            gaps = query_gaps(catalog)
            self.assertEqual(
                [row["service_id"] for row in gaps["missing_accountable"]],
                ["compute.virtual-machines"],
            )
            self.assertEqual(len(gaps["critical_missing_rto_rpo"]), 1)
            self.assertEqual(len(gaps["posture_missing_provenance"]), 2)

    def test_services_without_posture_are_not_provenance_gaps(self) -> None:
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack()],
                providers=[provider()],
                services=[
                    service(
                        "compute.virtual-machines",
                        name="Virtual Machines",
                        offerings=[
                            {
                                "id": "compute.virtual-machines.aws",
                                "name": "EC2",
                                "providers": ["aws"],
                            }
                        ],
                    )
                ],
                posture=[],
            )
            gaps = query_gaps(load_catalog(root))
            self.assertEqual(gaps["posture_missing_provenance"], [])
            self.assertEqual(gaps["critical_missing_rto_rpo"], [])


class ProviderConcentrationTests(unittest.TestCase):
    def test_counts_multi_provider_offerings_and_sorts(self) -> None:
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack(), stack("data", "Data")],
                providers=[
                    provider(),
                    provider("snowflake", "Snowflake Inc."),
                    provider("microsoft", "Microsoft"),
                ],
                services=[
                    service(
                        "compute.virtual-machines",
                        name="Virtual Machines",
                        offerings=[
                            {
                                "id": "compute.virtual-machines.aws",
                                "name": "EC2",
                                "providers": ["aws"],
                            },
                            {
                                "id": "compute.virtual-machines.azure",
                                "name": "Azure VM",
                                "providers": ["microsoft"],
                            },
                        ],
                    ),
                    service(
                        "data.cloud-warehouse",
                        name="Cloud Data Warehouse",
                        stack_name="Data",
                        offerings=[
                            {
                                "id": "data.cloud-warehouse.snowflake-aws",
                                "name": "Snowflake on AWS",
                                "providers": ["snowflake", "aws"],
                            }
                        ],
                    ),
                ],
            )
            rows = query_providers(load_catalog(root))
            by_id = {row["provider_id"]: row for row in rows}
            self.assertEqual(by_id["aws"]["offering_count"], 2)
            self.assertEqual(sorted(by_id["aws"]["stacks_affected"]), ["Compute", "Data"])
            self.assertEqual(by_id["snowflake"]["offering_count"], 1)
            self.assertEqual(rows[0]["provider_id"], "aws")


class ComplianceQueryTests(unittest.TestCase):
    def test_dora_report_does_not_claim_register(self) -> None:
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack()],
                providers=[provider()],
                services=[
                    service(
                        "compute.virtual-machines",
                        name="Virtual Machines",
                        offerings=[
                            {
                                "id": "compute.virtual-machines.aws",
                                "name": "EC2",
                                "providers": ["aws"],
                            }
                        ],
                    )
                ],
            )
            payload = query_compliance(load_catalog(root), "dora")
            self.assertIn("not a Register of Information", payload["disclaimer"])
            self.assertEqual(payload["rows"][0]["providers"], ["aws"])


class AgentContextTests(unittest.TestCase):
    def test_unknown_token_and_stripped_mappings(self) -> None:
        with TemporaryDirectory() as tmp:
            root = write_catalog(
                Path(tmp),
                stacks=[stack()],
                providers=[provider()],
                services=[
                    service(
                        "compute.virtual-machines",
                        name="Virtual Machines",
                        offerings=[
                            {
                                "id": "compute.virtual-machines.aws",
                                "name": "EC2",
                                "providers": ["aws"],
                            }
                        ],
                    )
                ],
                posture=[
                    {
                        "service_id": "compute.virtual-machines",
                        "privacy_classification": "not-assessed",
                        "operational_criticality": "important",
                        "offering_posture": [
                            {
                                "offering_id": "compute.virtual-machines.aws",
                                "rto": None,
                                "nist_control_status": "implemented",
                                "iso27001_controls": ["A.8.8"],
                            }
                        ],
                    }
                ],
            )
            payload = build_agent_context(load_catalog(root))
            service_row = payload["services"][0]
            self.assertEqual(payload["osm_version"], "1.3.0")
            self.assertEqual(
                service_row["operational_boundary"]["operational_criticality"],
                "important",
            )
            self.assertEqual(
                service_row["operational_boundary"]["privacy_classification"],
                "UNKNOWN",
            )
            offering = service_row["offerings"][0]
            self.assertEqual(offering["operational_boundary"]["rto"], "UNKNOWN")
            blob = json.dumps(payload)
            self.assertNotIn("nist_control_status", blob)
            self.assertNotIn("iso27001", blob)
            first = dumps_agent_context(payload)
            second = dumps_agent_context(build_agent_context(load_catalog(root)))
            self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
