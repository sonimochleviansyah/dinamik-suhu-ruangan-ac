import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

m = GEKKO(remote=False)                  # buat model GEKKO
m.time = np.linspace(0, 10, 401)         # titik waktu

# buat parameter GEKKO (step 0 ke 100 pada t = 2)
ustep = np.zeros(401)
ustep[81:] = 100.0
u = m.Param(value=ustep)

# buat variabel GEKKO
T = m.Var(30.0)
W = m.Var(31.0)

# buat persamaan GEKKO
m.Equation(0.5 * T.dt() == (W - T) - 0.5 * 0.12 * u)
m.Equation(4 * W.dt() == 32.0 - W)

# selesaikan ODE
m.options.IMODE = 4
m.solve(disp=False)

# plot hasil
plt.plot(m.time, ustep / 100 * 10 + 20, 'g:', label=r'$u(t)$ (skala)')
plt.plot(m.time, T, 'b-', label=r'$T(t)$ udara')
plt.plot(m.time, W, 'r--', label=r'$W(t)$ dinding')
plt.xlabel('$t$, (jam)')
plt.ylabel('Suhu (C)')
plt.legend(loc='best')
plt.show()
