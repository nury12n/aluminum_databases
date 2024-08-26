# Aluminum database development

Gonna make myself like aluminum. This will mainly be a collection of literature databases with some attempts at combining them. No model assessments will be made for now, maybe later.

This will also include databases for additional properties such as thermal conductivity, molar volume if possible.

### Folder structure
- databases - where all the databases are going. Each database will have a citation to the original paper. For merged databases, parameters should each have a citation
- pictures - any graphs related to the databases (e.g. phase diagrams, property vs. composition or temperature). These are mainly to validate against the papers I'm taking the databases from
- scripts - any python scripts to test the database
- models (not added yet) - custom pycalphad models for extra properties such as thermal conductivity

### Required packages for running any of the scripts
- numpy
- matplotlib
- pycalphad

### TODOs
- Fill out the phase information in the each database with space group, Strukturbericht, Pearson symbol and prototype to make it easier to know what models are compatible when merging databases
- Binary and ternary phase diagram plotting is there to compare with literature assessments. Should we also include isopleths when possible?
- Add links here to other large databases