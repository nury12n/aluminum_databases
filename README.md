# Aluminum database development

Gonna make myself like aluminum. This will mainly be a collection of literature databases with some attempts at combining them. No model assessments will be made for now, maybe later.

This will also include databases for additional properties such as thermal conductivity, molar volume if possible.

### Folder structure
- databases - where all the databases are going. Each database will have a citation to the original paper. For merged databases, each system will also have a citation.
- pictures - any graphs related to the databases (e.g. phase diagrams, property vs. composition or temperature). These are mainly to validate against the papers I'm taking the databases from
- scripts - any python scripts to test the database
- models - custom pycalphad models for extra properties

### Required packages
- numpy
- matplotlib
- pycalphad

### TODOs
- Each database should give the phase structure to make it easier to know which databases are compatible with each other
- Binary and ternary phase diagram plotting is there to compare with literature assessments. Should we also include isopleths when possible?