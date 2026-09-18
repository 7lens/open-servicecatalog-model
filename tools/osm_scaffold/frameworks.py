"""Discover OSM mapping frameworks from models/ and compliance/. Not a schema change."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Framework:
    id: str
    label: str
    path: str
    stack_fields: tuple[str, ...]
    notes: str


# Filename stem -> OSM mapping surface. Only fields that exist on frozen
# Technology Stack mappings are prompted. ArchiMate/ITIL/CSDM/TMF have no
# stack mapping fields; they can still be selected as applicable context.
_KNOWN: dict[str, Framework] = {
    "TOGAF": Framework(
        "togaf",
        "TOGAF",
        "models/architecture/TOGAF.md",
        ("togaf_domain",),
        "Optional togaf_domain on Technology Stack only.",
    ),
    "TBM": Framework(
        "tbm",
        "TBM",
        "models/architecture/TBM.md",
        ("tbm_tower", "tbm_sub_tower"),
        "Optional Resource Tower labels on Technology Stack only.",
    ),
    "ARCHIMATE": Framework(
        "archimate",
        "ArchiMate",
        "models/architecture/ARCHIMATE.md",
        (),
        "Conceptual mapping. No extra OSM stack field.",
    ),
    "ITIL": Framework(
        "itil",
        "ITIL",
        "models/service-management/ITIL.md",
        (),
        "Practice mapping. No extra OSM stack field.",
    ),
    "CSDM": Framework(
        "csdm",
        "ServiceNow CSDM",
        "models/service-management/CSDM.md",
        (),
        "CSDM mapping. Service Instance stays outside OSM.",
    ),
    "TMFORUM-TMF633": Framework(
        "tmf633",
        "TM Forum TMF633",
        "models/service-management/TMFORUM-TMF633.md",
        (),
        "Catalog mapping. No extra OSM stack field.",
    ),
    "ISO-27001": Framework(
        "iso27001",
        "ISO/IEC 27001",
        "compliance/ISO-27001.md",
        ("iso27001",),
        "Control ID locators on the stack. Not a Statement of Applicability.",
    ),
    "ISO-27701": Framework(
        "iso27701",
        "ISO/IEC 27701",
        "compliance/ISO-27701.md",
        ("iso27701",),
        "Optional locators. Not a PIMS.",
    ),
    "NIST-CSF": Framework(
        "nist",
        "NIST CSF",
        "compliance/NIST-CSF.md",
        ("nist_csf",),
        "Optional CSF Function list on the stack. Not a Profile.",
    ),
    "GDPR": Framework(
        "gdpr",
        "GDPR",
        "compliance/GDPR.md",
        ("gdpr",),
        "Optional locators. Not a Record of Processing Activities.",
    ),
    "DORA": Framework(
        "dora",
        "DORA",
        "compliance/DORA.md",
        ("dora",),
        "Optional stack pillar/criticality locators. OSM is not the RoI.",
    ),
    "EU-AI-ACT": Framework(
        "ai_act",
        "EU AI Act",
        "compliance/EU-AI-ACT.md",
        ("ai_act",),
        "Optional compatibility labels. Not Article 6 classification.",
    ),
}


def discover_frameworks(repo_root: Path) -> list[Framework]:
    """Scan models/ and compliance/ markdown (except README) in stable order."""
    found: list[Framework] = []
    seen: set[str] = set()
    for folder in (repo_root / "models", repo_root / "compliance"):
        if not folder.is_dir():
            continue
        for path in sorted(folder.rglob("*.md")):
            if path.name.upper() == "README.MD":
                continue
            stem = path.stem.upper()
            spec = _KNOWN.get(stem)
            if spec is None:
                rel = str(path.relative_to(repo_root))
                spec = Framework(
                    id=path.stem.lower().replace(" ", "-"),
                    label=path.stem.replace("-", " "),
                    path=rel,
                    stack_fields=(),
                    notes="Documented beside OSM. No extra stack field.",
                )
            if spec.id in seen:
                continue
            seen.add(spec.id)
            found.append(spec)
    return found
