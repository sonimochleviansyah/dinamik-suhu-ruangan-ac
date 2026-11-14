import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# fungsi yang mengembalikan dT/dt
def model(T, t):
    # u melompat dari 0 ke 100 pada t = 2
    if t < 2.0:
        u = 0
    else:
        u = 100
    dTdt = (32.0 - T) / 2.0 - 0.07 * u
    return dTdt

# kondisi awal
T0 = 30

# titik waktu
t = np.linspace(0, 10, 1000)

# selesaikan ODE
T = odeint(model, T0, t, tcrit=[2.0])

# plot hasil
plt.subplot(2, 1, 1)
plt.plot(t, T, 'r-')
plt.ylabel('Suhu $T(t)$, (C)')
plt.subplot(2, 1, 2)
plt.plot([0, 2, 2, 10], [0, 0, 100, 100], 'b-')
plt.ylabel('Daya AC $u(t)$, (%)')
plt.xlabel('$t$, (jam)')
plt.show()
