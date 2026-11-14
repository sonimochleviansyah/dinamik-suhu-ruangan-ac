import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

m = GEKKO(remote=False)           # buat model GEKKO
m.time = np.linspace(0, 10)       # titik waktu

t = m.Var(0.0)                    # buat waktu sebagai variabel
x = m.Var(30.0)                   # buat variabel x
y = m.Var(30.0)                   # buat variabel y

# buat persamaan GEKKO
m.Equation(t.dt() == 1)
m.Equation(x.dt() == -6 * m.exp(-0.5 * t))
m.Equation(y.dt() == -0.5 * y + 9)

# selesaikan ODE
m.options.IMODE = 4
m.options.NODES = 3
m.solve(disp=False)

# plot hasil
plt.plot(t, x, 'b-', label=r'$dx/dt=-6e^{-0.5t}$')
plt.plot(t, y, 'r--', label=r'$dy/dt=-0.5y+9$')
plt.ylabel('respon (C)')
plt.xlabel('waktu (jam)')
plt.legend(loc='best')
plt.show()
