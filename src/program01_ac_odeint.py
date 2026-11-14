import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# model suhu ruangan dengan AC
def ruangan(T, t, k, u):
    T_out = 32.0     # suhu udara luar (C)
    tau = 2.0        # konstanta waktu ruangan (jam)
    # hitung turunan suhu ruangan
    dTdt = (T_out - T) / tau - k * u
    return dTdt

# rentang waktu simulasi 10 jam, setiap 0.1 jam
ts = np.linspace(0, 10, 101)

# operasi AC
k = 0.07                # koefisien AC (C/jam per % daya)
u = np.zeros(101)       # u = daya AC (%)
u[20:70] = 100.0        # AC menyala antara jam ke-2 dan ke-7

# kondisi awal suhu ruangan
T0 = 30.0

# penyimpan hasil
z = np.zeros(101)
z[0] = T0

# simulasi dengan ODEINT
for i in range(100):
    daya = u[i]
    y = odeint(ruangan, T0, [0, 0.1], args=(k, daya))
    T0 = y[-1][0]          # ambil titik terakhir
    z[i + 1] = T0          # simpan suhu untuk plot

# plot hasil
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(ts, z, 'b-')
plt.ylabel('Suhu Ruangan $T(t)$, (C)')
plt.subplot(2, 1, 2)
plt.plot(ts, u, 'r--')
plt.ylabel('Daya AC $u(t)$, (%)')
plt.xlabel('$t$, (jam)')
plt.show()
