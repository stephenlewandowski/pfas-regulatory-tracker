# PFAS Environmental Law and Regulatory Tracker

This starter project uses a U.S.-federal-first architecture and extends it to overseas DoD environmental compliance. Its organizing model is:

**U.S. federal law and EPA/court actions → OEBGD → country-specific FGS → SOFA/international agreements → host-nation law and guidance → installation, component, and contractor obligations**

The first overseas modules are the Republic of Korea, Japan, and Germany/EU.

## Purpose

The tracker is intended to answer six questions for each PFAS development:

1. What changed?
2. At which legal or policy layer did it change?
3. What is its legal effect and current status?
4. Where and to whom does it apply?
5. Was it incorporated into, or does it require review of, a country FGS?
6. What action, decision, or follow-up is warranted?

OEBGD and FGS records are kept separate from host-nation law. An FGS is a DoD compliance instrument that reconciles the OEBGD baseline with applicable host-nation standards, international agreements, and other governing requirements; it is not itself a substitute for the host-nation legal record.

## Current starter scope

- U.S. federal: CERCLA, SDWA, TSCA, RCRA, CWA, EPCRA, EPA PFAS actions, Federal Register notices, and federal court posture.
- Overseas: DoD environmental policy, OEBGD volumes and changes, country FGS revisions, SOFA/international agreements, host-nation legal developments, and installation obligations.
- Countries: Republic of Korea, Japan, and Germany/EU.
- Operational themes: drinking water, wastewater, AFFF and firefighting foam, hazardous materials, waste, spills, soil and groundwater, laboratories, contracts, and remediation.

The current seed set was checked against official sources on 2026-08-20. It is an architecture and evidence register, not a legal opinion.

## Quick validation

From this project directory, run:

```bash
python3 scripts/validate_project.py
```

The validator uses only the Python standard library.

## Project structure

```text
data/
  events.json          Legal, regulatory, FGS, and policy developments
  jurisdictions.json   Geographic and institutional jurisdictions
  layers.json          The six-layer core model
  obligations.json     Initial operational obligation templates
  relationships.json   Cross-layer links and review dependencies
  sources.json         Evidence register
docs/
  architecture.md      Model, scope, and relationship rules
  data-dictionary.md   Field definitions and controlled vocabularies
  source-protocol.md   Source, translation, and review protocol
schema/
  record-schema.json   Machine-readable minimum record contract
scripts/
  validate_project.py  Structural and relationship validation
```

## Initial build sequence

1. Stabilize the six-layer data model and source hierarchy.
2. Expand the U.S. federal event register and court-posture records.
3. Complete the South Korea module as the first country pilot.
4. Add the Japan PFAS drinking-water and chemical-control developments.
5. Validate the current Germany/EU FGS source and add German/EU requirements.
6. Map developments to installation, component, contractor, and decision obligations.

## Governing source anchors

- [DoDI 4715.05, Environmental Compliance at Installations Outside the United States](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/471505p.pdf?ver=2017-10-05-073242-057)
- [Current DoD overseas environmental manuals](https://www.esd.whs.mil/directives/issuances/dodm/)
- [OEBGD Volume 1, Change 1](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodm/471505_vol1.PDF?ver=WfxNjtSCrRUD7BKxN5turg%3D%3D)
- [DENIX Final Governing Standards framework](https://www.denix.osd.mil/international/policy/final-governing-standards/)
- [USFK publications](https://www.usfk.mil/Resources/Publications/)
- [USFJ Japan Environmental Governing Standards](https://www.usfj.mil/Resources/JEGS/)
- [Japan Ministry of the Environment PFAS drinking-water action](https://www.env.go.jp/press/press_00075.html)
- [German Environment Agency drinking-water PFAS limits](https://www.umweltbundesamt.de/en/press/pressinformation/new-drinking-water-ordinance-ensures-high-quality)
- [EU REACH firefighting-foam restriction](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202501988)

