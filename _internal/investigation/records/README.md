# OSM investigation records

These YAML files are a **model test suite**. They attempt to encode
publicly researched provider and service facts in the **frozen OSM
1.3.0 schema** without changing that schema.

They are **not**:

- a real enterprise catalog
- a recommended taxonomy
- a vendor register for regulatory filing
- a replacement for `examples/`
- a claim of certification, DORA compliance, GDPR compliance, or
  AI Act classification

Public learning catalog: `examples/reference-estate/`.
These files remain the investigation test suite, including
application-boundary records that were not promoted.

## How to read them

1. Every ICT Provider `certifications` entry is a **published
   program name**. Scope is in provenance and in
   `../research_matrix.md`. Do not treat a badge as covering every
   service, region, edition, or customer deployment.
2. Customer-dependent fields (`contract_*`, `gdpr_dpa_signed`,
   `dora_notification_clause`, `risk_level`, `rto`, `rpo`,
   `operational_criticality`, data classification) are **left unset
   or null** on purpose.
3. `substitutability` is a **market-level observation** where
   Flexera 2025 supports it; it is not a customer risk score.
4. Vendor SLAs are offering **characteristics**
   (`vendor_availability_sla`). They are not
   `availability_target`.
5. `accountable: Reference Estate Service Owner` is a placeholder
   role. OSM requires an accountable Service Owner; this
   investigation is not an organisation.
6. SAP S/4HANA Cloud and Salesforce Sales Cloud are encoded only to
   **stress the application boundary**. They are not a
   recommendation to catalog ERP/CRM as OSM Services.

## Validate

From the repository root:

```bash
python3 validation/validate.py --catalog _internal/investigation/records
```
