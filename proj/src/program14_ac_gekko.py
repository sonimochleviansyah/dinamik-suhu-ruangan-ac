import numpy as np
from gekko import GEKKO
import matplotlib.pyplot as plt

T_out, tau, k = 32.0, 2.0, 0.07

m = GEKKO(remote=False)
m.time = np.linspace(0, 10, 101)          # titik waktu

# AC menyala jam ke-2 s.d. 7 (GEKKO membaca input di akhir interval, digeser 1 langkah)
u_g = np.zeros(101)
u_g[21:71] = 100.0
u = m.Param(value=u_g)

T = m.Var(30.0)                           # suhu awal 30 C
m.Equation(T.dt() == (T_out - T) / tau - k * u)

m.options.IMODE = 4
m.solve(disp=False)

plt.plot(m.time, T, 'b-')
plt.ylabel('Suhu Ruangan $T(t)$, (C)')
plt.xlabel('$t$, (jam)')
plt.show()
print('GEKKO: T(7)=%.3f  T(10)=%.3f' % (T.value[70], T.value[100]))
