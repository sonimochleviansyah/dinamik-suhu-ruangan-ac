import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# model suhu ruangan dengan AC
def ruangan(T, t, u):
    T_out = 32.0
    tau = 2.0
    k = 0.07
    return (T_out - T) / tau - k * u

# batas termostat
T_on = 26.0       # AC menyala jika T > 26 C
T_off = 24.0      # AC mati jika T < 24 C

# waktu simulasi 10 jam, setiap 0.01 jam
dt = 0.01
ts = np.arange(0, 10 + dt, dt)

# penyimpan hasil
T = np.zeros(len(ts))
u = np.zeros(len(ts))
T[0] = 30.0                 # suhu awal
status = 0.0                # 0 = AC mati, 100 = AC menyala

# simulasi dengan ODEINT
for i in range(1, len(ts)):
    if T[i - 1] > T_on:
        status = 100.0
    elif T[i - 1] < T_off:
        status = 0.0
    u[i] = status
    y = odeint(ruangan, T[i - 1], [0, dt], args=(status,))
    T[i] = y[-1][0]

# plot hasil
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(ts, T, 'b-')
plt.axhline(T_on, color='r', linestyle='--')
plt.axhline(T_off, color='g', linestyle='--')
plt.ylabel('Suhu Ruangan $T(t)$, (C)')
plt.subplot(2, 1, 2)
plt.plot(ts, u, 'r-')
plt.ylabel('Daya AC $u(t)$, (%)')
plt.xlabel('$t$, (jam)')
plt.show()

print('AC menyala total = %.2f jam' % (u.sum() * dt / 100))
