"""
Script to plot a step diagram
"""
DATABASE = "Al-Cu-Fe-Mg-Si.tdb"
COMPONENTS = ["AL", "FE", "MG", "SI", "VA"]
PHASES = None

import os
import matplotlib.pyplot as plt
from pycalphad import variables as v
from pycalphad.mapping import StepStrategy, plot_step

conds = {v.T: (500, 4000, 10), v.P: 101325, v.X("AL"): 0.4976, v.X("FE"): 0.00242, v.X("MG"): 0.0111}

db_path = os.path.join("databases", DATABASE)
strategy = StepStrategy(db_path, COMPONENTS, PHASES, conds)
strategy.initialize()
strategy.do_map()

fig, ax = plt.subplots()
plot_step(strategy, ax=ax)
fig.tight_layout()

plt.show()