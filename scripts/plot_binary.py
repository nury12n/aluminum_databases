"""
Script to plot a binary and save to pictures folder
"""
DATABASE = "Cu-Fe-Si_Soldi_2019.tdb"
COMPONENTS = ["CU", "SI", "VA"]
#PHASES = ['LIQUID', 'BCC_B2', 'DIAMOND_A4', 'FESI2_L', 'FESI2_H', 'FE5SI3', 'FESI', 'FE2SI']
PHASES = None

TEMPERATURE_LIMITS = [300, 4000]
TEMPERATURE_STEP = 10
PRESSURE = 101325
X = "SI"

SAVE_FIGURE = False


import os
import matplotlib.pyplot as plt
from pycalphad import variables as v
from pycalphad.mapping import BinaryStrategy, plot_binary

conds = {v.T: (TEMPERATURE_LIMITS[0], TEMPERATURE_LIMITS[1], TEMPERATURE_STEP), v.P: PRESSURE, v.X(X): (0, 1, 0.01)}

db_path = os.path.join("databases", DATABASE)
strategy = BinaryStrategy(db_path, COMPONENTS, PHASES, conds)
strategy.initialize()
strategy.do_map()

fig, ax = plt.subplots()
plot_binary(strategy, ax=ax)
fig.tight_layout()

if SAVE_FIGURE:
    db_title = DATABASE.split(".")[0]
    element_title = '-'.join(sorted(list(set(COMPONENTS) - {"VA"})))
    output_file = os.path.join("pictures", "binaries", f"{element_title}_{db_title}.png")
    fig.savefig(output_file, dpi=200)

plt.show()