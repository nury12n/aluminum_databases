"""
Script to plot a ternary and save to pictures folder
"""
DATABASE = "Al-Cu-Fe-Mg-Si.tdb"
COMPONENTS = ["AL", "CU", "FE", "VA"]
PHASES = None

TEMPERATURE = 1000+273
PRESSURE = 101325
X = "CU"
Y = "AL"

SAVE_FIGURE = False


import os
import matplotlib.pyplot as plt
from pycalphad import Database, variables as v
from pycalphad.plot import triangular
from pycalphad.core.utils import unpack_species, filter_phases
from pycalphad.mapping import TernaryStrategy, plot_ternary

db = Database('databases/' + DATABASE)
PHASES = filter_phases(db, unpack_species(db, COMPONENTS))

conds = {v.T: TEMPERATURE, v.P: PRESSURE, v.X(X): (0, 1, 0.01), v.X(Y): (0, 1, 0.01)}

db_path = os.path.join("databases", DATABASE)
strategy = TernaryStrategy(db_path, COMPONENTS, PHASES, conds, GLOBAL_MIN_NUM_CANDIDATES=10000)
#strategy.add_nodes_from_conditions({v.T: TEMPERATURE, v.P: PRESSURE, v.X(X): 0.3, v.X(Y):0.3})
strategy.initialize()
strategy.do_map()

fig, ax = plt.subplots(subplot_kw = {"projection": "triangular"})
plot_ternary(strategy, ax=ax, x=v.X(X), y=v.X(Y), label_nodes=True)
fig.tight_layout()

if SAVE_FIGURE:
    db_title = DATABASE.split(".")[0]
    element_title = '-'.join(sorted(list(set(COMPONENTS) - {"VA"})))
    output_file = os.path.join("pictures", "ternaries", f"{element_title}_{TEMPERATURE}_{db_title}.png")
    fig.savefig(output_file, dpi=200)

plt.show()