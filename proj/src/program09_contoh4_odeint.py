import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# fungsi yang mengembalikan dz/dt
def model(z, t):
    dxdt = -6.0 * np.exp(-0.5 * t)
    dydt = -0.5 * z[1] + 9.0
    dzdt = [dxdt, dydt]
    return dzdt

# kondisi awal
z0 = [30, 30]

# titik waktu
t = np.linspace(0, 10)

# selesaikan ODE
z = odeint(model, z0, t)

# plot hasil
plt.plot(t, z[:, 0], 'b-', label=r'$\frac{dx}{dt}=-6\,\exp(-0.5t)$')
plt.plot(t, z[:, 1], 'r--', label=r'$\frac{dy}{dt}=-0.5y+9$')
plt.ylabel('$x(t),\\; y(t)$, (C)')
plt.xlabel('$t$, (jam)')
plt.legend(loc='best')
plt.show()
