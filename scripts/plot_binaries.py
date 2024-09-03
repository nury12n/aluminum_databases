"""
Script to plot a all pair-wise combinations of a set of elements
"""
DATABASE = "Al-Cu-Fe-Mg-Si.tdb"
COMPONENTS = ["AL", "CU", "FE", "MG", "SI"]
PHASES = None

TEMPERATURE_LIMITS = [300, 4000]
TEMPERATURE_STEP = 10
PRESSURE = 101325

import os
from itertools import combinations
import matplotlib.pyplot as plt
from pycalphad import variables as v
from pycalphad.mapping import BinaryStrategy, plot_binary

for comps in combinations(COMPONENTS, 2):
    components = list(comps) + ["VA"]
    conds = {v.T: (TEMPERATURE_LIMITS[0], TEMPERATURE_LIMITS[1], TEMPERATURE_STEP), v.P: PRESSURE, v.X(components[1]): (0, 1, 0.01)}

    db_path = os.path.join("databases", DATABASE)
    strategy = BinaryStrategy(db_path, components, PHASES, conds)
    strategy.initialize()
    strategy.do_map()

    fig, ax = plt.subplots()
    plot_binary(strategy, ax=ax)
    fig.tight_layout()

plt.show()