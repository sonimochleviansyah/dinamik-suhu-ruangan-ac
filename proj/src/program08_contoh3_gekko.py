import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

m = GEKKO(remote=False)                  # buat model GEKKO
m.time = np.linspace(0, 10, 1001)        # titik waktu

# buat parameter GEKKO (step 0 ke 100 pada t = 2)
ustep = np.zeros(1001)
ustep[201:] = 100.0
u = m.Param(value=ustep)

T = m.Var(30.0)                          # buat variabel GEKKO
m.Equation(2 * T.dt() == (32.0 - T) - 2 * 0.07 * u)   # buat persamaan GEKKO

# selesaikan ODE
m.options.IMODE = 4
m.solve(disp=False)

# plot hasil
plt.subplot(2, 1, 1)
plt.plot(m.time, T, 'r-')
plt.ylabel('Suhu $T(t)$, (C)')
plt.subplot(2, 1, 2)
plt.plot(m.time, ustep, 'b-')
plt.ylabel('Daya AC $u(t)$, (%)')
plt.xlabel('$t$, (jam)')
plt.show()
