import os
from pycalphad import Workspace, Database, variables as v
from pycalphad.property_framework.metaproperties import IsolatedPhase
import matplotlib.pyplot as plt

DATABASE = "Al-Fe-Si_Liu_1999.tdb"
COMPONENTS = ["FE", "SI", "VA"]
PHASES = ['LIQUID', 'BCC_A2', 'FCC_A1']

TEMPERATURE = 1400
PRESSURE = 101325
X = "SI"

conditions = {v.T: TEMPERATURE, v.P: PRESSURE, v.X(X): (0, 1, 0.01)}
wks = Workspace(os.path.join('databases', DATABASE), COMPONENTS, PHASES, conditions=conditions)

fig = plt.figure()
ax = fig.add_subplot()

x = wks.get(v.X(X))
ax.set_xlabel(f"{v.X(X).display_name} [{v.X(X).display_units}]")

for phase_name in wks.phases:
    prop = IsolatedPhase(phase_name, wks)(f'GM({phase_name})')
    prop.display_name = f'GM({phase_name})'
    ax.plot(x, wks.get(prop), label=prop.display_name)
ax.legend()
plt.show()

