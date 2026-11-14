import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

tau = 2.0          # konstanta waktu ruangan (jam)
k = 0.07           # koefisien pendinginan AC (C/jam per %)
P_ac = 0.9         # daya listrik AC saat menyala (kW)

# suhu udara luar berubah sepanjang hari (maksimum jam 15.00)
def T_luar(t):
    return 30.0 + 4.0 * np.sin(2 * np.pi * (t - 9.0) / 24.0)

# model suhu ruangan
def ruangan(T, t, u):
    return (T_luar(t) - T) / tau - k * u

# waktu simulasi 24 jam, setiap 0.01 jam
dt = 0.01
ts = np.arange(0, 24 + dt, dt)

# pilihan setpoint termostat: (batas OFF, batas ON)
pilihan = [(21, 23), (23, 25), (25, 27)]
warna = ['b', 'g', 'r']

plt.figure(figsize=(8, 6))
for (T_off, T_on), w in zip(pilihan, warna):
    T = np.zeros(len(ts))
    u = np.zeros(len(ts))
    T[0] = 30.0
    status = 0.0
    for i in range(1, len(ts)):
        if T[i - 1] > T_on:
            status = 100.0
        elif T[i - 1] < T_off:
            status = 0.0
        u[i] = status
        y = odeint(ruangan, T[i - 1], [ts[i - 1], ts[i]], args=(status,))
        T[i] = y[-1][0]
    energi = np.cumsum(u) * dt / 100 * P_ac          # energi listrik (kWh)
    label = '%d-%d C' % (T_off, T_on)
    plt.subplot(2, 1, 1)
    plt.plot(ts, T, w + '-', label=label)
    plt.subplot(2, 1, 2)
    plt.plot(ts, energi, w + '-', label=label)
    print('Setpoint %s : AC menyala %.2f jam, energi %.2f kWh' %
          (label, u.sum() * dt / 100, energi[-1]))

plt.subplot(2, 1, 1)
plt.plot(ts, T_luar(ts), 'k:', label='suhu luar')
plt.ylabel('Suhu Ruangan $T(t)$, (C)')
plt.legend(frameon=False, ncol=4, loc='lower center', bbox_to_anchor=(0.5, 1.0))
plt.subplot(2, 1, 2)
plt.ylabel('Energi Listrik, (kWh)')
plt.xlabel('$t$, (jam)')
plt.legend(frameon=False)
plt.show()
