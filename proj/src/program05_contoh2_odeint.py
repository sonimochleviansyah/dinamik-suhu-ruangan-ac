import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# fungsi yang mengembalikan dy/dt
def model(y, t, k):
    dydt = -k * y
    return dydt

# kondisi awal
y0 = 10

# titik waktu
t = np.linspace(0, 10)

# selesaikan ODE
k = 0.25
y1 = odeint(model, y0, t, args=(k,))
k = 0.5
y2 = odeint(model, y0, t, args=(k,))
k = 1.0
y3 = odeint(model, y0, t, args=(k,))

# plot hasil
plt.plot(t, y1, 'r-', label=r'$k=0.25$')
plt.plot(t, y2, 'b--', label=r'$k=0.5$')
plt.plot(t, y3, 'g:', label=r'$k=1.0$')
plt.xlabel('$t$, (jam)')
plt.ylabel('$y(t)$, (C)')
plt.legend()
plt.show()
