import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# fungsi yang mengembalikan dz/dt
def model(z, t, u):
    T = z[0]                          # suhu udara ruangan
    W = z[1]                          # suhu dinding
    dTdt = ((W - T) - 0.5 * 0.12 * u) / 0.5
    dWdt = (32.0 - W) / 4.0
    dzdt = [dTdt, dWdt]
    return dzdt

# kondisi awal
z0 = [30, 31]

# jumlah titik waktu
n = 401

# titik waktu
t = np.linspace(0, 10, n)

# input step: AC menyala 100% mulai jam ke-2
u = np.zeros(n)
u[80:] = 100.0

# penyimpan hasil
T = np.empty_like(t)
W = np.empty_like(t)
T[0] = z0[0]
W[0] = z0[1]

# selesaikan ODE
for i in range(1, n):
    tspan = [t[i - 1], t[i]]
    z = odeint(model, z0, tspan, args=(u[i - 1],))
    T[i] = z[1][0]
    W[i] = z[1][1]
    z0 = z[1]

# plot hasil
plt.plot(t, u / 100 * 10 + 20, 'g:', label=r'$u(t)$ (skala)')
plt.plot(t, T, 'b-', label=r'$T(t)$ udara')
plt.plot(t, W, 'r--', label=r'$W(t)$ dinding')
plt.ylabel('Suhu (C)')
plt.xlabel('$t$, (jam)')
plt.legend(loc='best')
plt.show()
