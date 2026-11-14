import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

m = GEKKO(remote=False)           # buat model GEKKO
k = 0.5                           # konstanta
y = m.Var(10.0)                   # buat variabel GEKKO
m.Equation(y.dt() == -k * y)      # buat persamaan GEKKO
m.time = np.linspace(0, 10)       # titik waktu

# selesaikan ODE
m.options.IMODE = 4
m.solve(disp=False)

# plot hasil
plt.plot(m.time, y)
plt.xlabel('$t$, (jam)')
plt.ylabel('$y(t)$, (C)')
plt.show()
