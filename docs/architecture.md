# Architecture

## Core relationship

The tracker models PFAS developments as a chain of authority and implementation rather than as a flat list of country laws:

```text
U.S. federal law and EPA/court actions
        ↓
DoD overseas policy and OEBGD
        ↓
Country-specific FGS
        ↓
SOFA and international agreements
        ↓
Host-nation law and guidance
        ↓
Installation, component, and contractor obligations
```

The arrows represent a review and implementation relationship. They do not mean that every lower-layer document automatically incorporates every upper-layer provision or that every host-nation law applies identically to every DoD activity.

## Layer rules

### U.S. federal law and EPA/court actions

This is the primary spine. Records include statutes, rules, determinations, guidance, enforcement policies, Federal Register notices, agency interpretations, and federal court decisions. Each record must distinguish publication, effective, compliance, and litigation dates where those dates differ.

### OEBGD

OEBGD records identify the applicable volume, version, change, effective date, subject area, and whether a country FGS has considered the change. OEBGD is a DoD baseline for overseas installations and is not a host-nation statute.

The tracker must flag a possible OEBGD-to-FGS currency gap. It must not resolve that gap automatically as a legal conclusion. A gap should create a revalidation task for the responsible Lead Environmental Component and an interim more-protective-standard review where the governing policy requires one.

### Country-specific FGS

The generic FGS type has country-specific names:

| Country | FGS name used in the initial module | Lead Environmental Component | Initial public version |
|---|---|---|---|
| Republic of Korea | Korea Environmental Governing Standards, also called EGS/KEGS | USFK | 2024 |
| Japan | Japan Environmental Governing Standards, JEGS | USFJ | 2024 |
| Germany | German Final Governing Standards, GFGS | European theater structure; current responsible authority to verify | Publicly identified 2019 version; currency not yet verified |

An FGS record must include its version, effective or receipt date, review cycle, source status, applicable installations or facility status, and relationship to the OEBGD version used to develop it.

### SOFA and international agreements

SOFA and related bilateral arrangements are a distinct layer because they can affect permits, access, environmental responsibility, contractor obligations, host-nation consultation, and applicability of local requirements. The tracker should record the specific provision and avoid treating the SOFA as a general exemption from all host-nation environmental requirements.

### Host-nation law and guidance

Each country module should track national law, implementing regulations, ordinances, standards, agency guidance, monitoring programs, and relevant court or administrative decisions. Original-language sources are primary evidence. English translations are supporting aids and must carry a translation-status field.

Germany is modeled as Germany plus an EU overlay because EU regulations and restrictions can directly affect operations in Germany. Japanese prefectural and municipal requirements, and German Länder requirements, should be collected when facility status, contractor activity, limited-use areas, or off-installation work makes them potentially applicable.

### Installation, component, and contractor obligations

The bottom layer converts legal and policy records into operational actions, such as sampling, reporting, storage, procurement, waste shipment, fire-training restrictions, spill response, laboratory qualification, contract clauses, or a required LEC determination. These are obligation records, not new legal authorities.

## Record relationship rules

The minimum relationships are:

- a federal, OEBGD, FGS, SOFA, or host-nation record may support one or more obligations;
- an OEBGD change may require review of several country FGS records;
- a host-nation change may trigger FGS revalidation, installation review, or both;
- an FGS provision may map to a host-nation provision, a SOFA provision, an OEBGD provision, or an installation obligation;
- a court or agency action may change the status of an earlier rule without replacing the historical record;
- a compliance record must be separated from a contamination or remediation record.

## Applicability dimensions

Applicability is multidimensional and should not be reduced to a country field. At minimum, track:

- exclusive-use facility;
- joint-use or limited-use facility;
- installation-wide activity;
- tenant or supported activity;
- contractor or vendor;
- off-installation activity;
- aircraft, vessel, or mobile support;
- waste exported to or handled in the host nation.

## Initial country priorities

The first operational crosswalks should address:

- drinking-water and wastewater criteria;
- groundwater and soil screening or cleanup criteria;
- AFFF storage, use, replacement, training, and disposal;
- hazardous-material and chemical-product controls;
- hazardous-waste classification, manifests, shipment, and treatment;
- spill reporting and emergency response;
- laboratory accreditation, analytical methods, and quality assurance;
- contractor permits and procurement restrictions.

