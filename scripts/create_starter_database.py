"""
Script for generate a template database with the elements and functions
taken from a unary database

TODO: make the output a bit neater for the symbols, right now pycalphad
      bunches the symbols together
"""
UNARY_DATABASE = "starter_databases/unary50.tdb"
OUTPUT_DATABASE = "Al-Ce_test.tdb"
COMPONENTS = ["AL", "CE"]

# These should be all the possible templates in the unary50.tdb (SGTE Unary V5)
FUNCTION_TEMPLATES = ["GHSER", "GFCC", "GHCP", "GBCC", "GLIQ", "GDIA", "GRHOMB", "GRED"]


import os
from pycalphad import Database

dbf = Database(UNARY_DATABASE)
dbf_out = Database()

extra_comps = ["VA", "/-"]
for c in extra_comps:
    dbf_out.elements |= {c}
    if c in dbf.refstates:
        dbf_out.refstates[c] = dbf.refstates[c]

for c in COMPONENTS:
    dbf_out.elements |= {c}
    if c in dbf.refstates:
        dbf_out.refstates[c] = dbf.refstates[c]
    for temp in FUNCTION_TEMPLATES:
        func_name = temp + c
        if func_name in dbf.symbols:
            dbf_out.symbols[func_name] = dbf.symbols[func_name]

out_path = os.path.join('databases', OUTPUT_DATABASE)
dbf_out.to_file(out_path)

