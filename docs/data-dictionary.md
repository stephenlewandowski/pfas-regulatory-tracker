# Data dictionary

## Common record fields

| Field | Meaning |
|---|---|
| `id` | Stable project identifier. Do not reuse an identifier for a different instrument or development. |
| `title` | Short descriptive title. |
| `record_type` | Type of development, source, relationship, or obligation. |
| `layer_id` | One of the six core-model layers. |
| `jurisdiction_id` | Jurisdiction or institutional setting. |
| `status` | Current legal, policy, or review posture. |
| `publication_date` | Date the source or instrument was published or issued. |
| `effective_date` | Date the provision became effective, if applicable. |
| `compliance_date` | Date a regulated party must comply, if different. |
| `date_precision` | `day`, `month`, `year`, or `unknown`. |
| `summary` | Evidence-based description of what changed. |
| `determination` | Current conclusion supported by the source. |
| `operational_relevance` | Why an installation, component, contractor, or decision-maker may care. |
| `source_ids` | Evidence-register identifiers. |
| `parent_ids` | Upstream records in the core model. |
| `last_verified` | Date the record was last checked against its source. |
| `review_state` | `verified`, `needs_revalidation`, `discovery_only`, or `superseded`. |

## Controlled status vocabulary

The initial controlled vocabulary is:

`proposed`, `final`, `effective`, `effective_under_litigation`, `guidance`, `monitoring`, `pending`, `superseded`, `historical`, `needs_revalidation`, `discovery_only`.

Status and legal effect are separate. For example, an effective technical standard may be binding for an installation through an FGS, while the same underlying host-nation document may be guidance outside that FGS context.

## Evidence and uncertainty

Use `fact`, `inference`, and `verification_need` fields when a record has an operational implication that is not stated verbatim in the source. Do not convert a source comparison into a definitive legal conclusion without the responsible LEC or other competent authority.

## Date handling

When a source gives only a month or year, use the first day of that period in machine-readable fields and set `date_precision` accordingly. Preserve the original date expression in `date_note`.

## Source fields

Sources must identify:

- issuing authority;
- original-language title where relevant;
- source URL;
- source type;
- officiality status;
- language;
- publication or effective date if known;
- the reason the source is being retained;
- whether it is suitable for definitive use or discovery only.

