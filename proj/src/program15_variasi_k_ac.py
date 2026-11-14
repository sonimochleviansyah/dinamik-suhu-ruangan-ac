import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# model suhu ruangan dengan AC
def ruangan(T, t, k, u):
    T_out, tau = 32.0, 2.0
    return (T_out - T) / tau - k * u

ts = np.linspace(0, 10, 101)
u = np.zeros(101)
u[20:70] = 100.0               # AC menyala jam ke-2 s.d. ke-7

# fungsi simulasi untuk nilai k tertentu
def simulasi(k, T0=30.0):
    z = np.zeros(101)
    z[0] = T0
    for i in range(100):
        y = odeint(ruangan, T0, [0, 0.1], args=(k, u[i]))
        T0 = y[-1][0]
        z[i + 1] = T0
    return z

# plot hasil
plt.plot(ts, simulasi(0.03), 'r-', label=r'$k=0.03$')
plt.plot(ts, simulasi(0.05), 'b--', label=r'$k=0.05$')
plt.plot(ts, simulasi(0.07), 'g:', label=r'$k=0.07$')
plt.xlabel('$t$, (jam)')
plt.ylabel('Suhu Ruangan $T(t)$, (C)')
plt.legend()
plt.show()
