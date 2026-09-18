"""Shared modelling dictionaries for lint and scaffold.

These are tooling conventions, not OSM schema. They encode the
anti-patterns in the OSM usability brief §10 so CLIs can refuse
product-named Services, request-catalog Offerings, and vendor-tower
Stacks without changing the frozen model.
"""

from __future__ import annotations

# Product / project / suite tokens that must not be a Service id
# segment or a Service name. Values are the suggested capability
# service id (when one exists) and a short product label for advice.
PRODUCT_SERVICE_TOKENS: dict[str, tuple[str, str]] = {
    "eks": ("compute.kubernetes", "Amazon EKS"),
    "aks": ("compute.kubernetes", "Azure Kubernetes Service"),
    "gke": ("compute.kubernetes", "Google Kubernetes Engine"),
    "openshift": ("compute.kubernetes", "OpenShift"),
    "ec2": ("compute.virtual-machines", "Amazon EC2"),
    "gce": ("compute.virtual-machines", "Google Compute Engine"),
    "vmware": ("compute.virtual-machines", "VMware"),
    "lambda": ("compute.functions", "AWS Lambda"),
    "s3": ("storage.object-storage", "Amazon S3"),
    "rds": ("db.managed-relational", "Amazon RDS"),
    "dynamodb": ("db.managed-nosql", "Amazon DynamoDB"),
    "bigquery": ("data.analytics-warehouse", "BigQuery"),
    "snowflake": ("data.cloud-warehouse", "Snowflake"),
    "m365": ("(decompose the suite)", "Microsoft 365"),
    "microsoft-365": ("(decompose the suite)", "Microsoft 365"),
    "office365": ("(decompose the suite)", "Microsoft 365"),
    "office-365": ("(decompose the suite)", "Microsoft 365"),
}

# Offering slug / name tokens that mean an ITSM request type, not a
# technological variant.
ITSM_OFFERING_TOKENS: tuple[str, ...] = (
    "request",
    "ticket",
    "reset",
    "mfa",
    "provisioning",
)

# Stack ids / normalised names that are vendor towers, not competency
# domains of the adopting organisation.
VENDOR_STACK_TOKENS: frozenset[str] = frozenset(
    {
        "aws",
        "amazon",
        "amazon-web-services",
        "azure",
        "microsoft",
        "m365",
        "microsoft-365",
        "office365",
        "gcp",
        "google",
        "google-cloud",
        "oracle",
        "ibm",
        "alibaba",
        "salesforce",
        "servicenow",
    }
)

# Capability service slugs where a seller is almost never intrinsic.
# Service-level providers on these should live on Offerings instead.
NON_INTRINSIC_SERVICE_SLUGS: frozenset[str] = frozenset(
    {
        "kubernetes",
        "virtual-machines",
        "object-storage",
        "functions",
        "managed-relational",
        "backup",
        "landing-zone",
        "vpc",
        "container-service",
        "configuration-automation",
    }
)

CLOUD_AUTHORIZATION_TOKENS: frozenset[str] = frozenset(
    {
        "aws-iam",
        "gcp-iam",
        "cloud-iam",
        "azure-rbac",
        "cloud-authorization",
        "iam-identity-center",
    }
)

WORKFORCE_IDP_TOKENS: frozenset[str] = frozenset(
    {
        "entra",
        "entra-id",
        "okta",
        "okta-workforce",
        "azure-ad",
        "directory-idp",
        "workforce-idp",
        "auth0",
    }
)

# Characteristic names that often duplicate providers[].
PROVIDER_DUPLICATE_CHAR_NAMES: frozenset[str] = frozenset(
    {
        "deployment_environment",
        "cloud",
        "cloud_provider",
        "provider",
        "vendor",
        "hyperscaler",
    }
)

PROVIDER_VALUE_ALIASES: dict[str, str] = {
    "aws": "aws",
    "amazon": "aws",
    "amazon-web-services": "aws",
    "azure": "microsoft",
    "microsoft": "microsoft",
    "ms": "microsoft",
    "gcp": "google-cloud",
    "google": "google-cloud",
    "google-cloud": "google-cloud",
}

VENDOR_SLA_CHAR_NAMES: frozenset[str] = frozenset(
    {
        "vendor_availability_sla",
        "vendor_sla",
        "sla",
        "availability_sla",
    }
)


def tokenize(value: str) -> list[str]:
    """Lowercase hyphen/underscore/space/dot segments."""
    raw = value.strip().lower().replace("_", "-").replace(".", "-").replace(" ", "-")
    return [part for part in raw.split("-") if part]


def normalised_name(value: str) -> str:
    return "-".join(tokenize(value))
