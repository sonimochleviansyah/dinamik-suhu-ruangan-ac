import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

m = GEKKO(remote=False)           # buat model GEKKO
k = m.Param()                     # konstanta
y = m.Var(10.0)                   # buat variabel GEKKO
m.Equation(y.dt() == -k * y)      # buat persamaan GEKKO
m.time = np.linspace(0, 10)       # titik waktu

# selesaikan ODE dan plot
m.options.IMODE = 4
m.options.TIME_SHIFT = 0

k.value = 0.25
m.solve(disp=False)
plt.plot(m.time, y.value, 'r-', linewidth=2, label='k=0.25')

k.value = 0.5
m.solve(disp=False)
plt.plot(m.time, y.value, 'b--', linewidth=2, label='k=0.5')

k.value = 1.0
m.solve(disp=False)
plt.plot(m.time, y.value, 'g:', linewidth=2, label='k=1.0')

plt.xlabel('$t$, (jam)')
plt.ylabel('$y(t)$, (C)')
plt.legend()
plt.show()
