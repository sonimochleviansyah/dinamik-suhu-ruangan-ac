from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# fungsi yang mengembalikan dy/dt
def model(y, t):
    k = 0.5
    dydt = -k * y
    return dydt

# kondisi awal
y0 = 10

# titik waktu
t = np.linspace(0, 10)

# selesaikan ODE
y = odeint(model, y0, t)

# plot hasil
plt.plot(t, y)
plt.xlabel('$t$, (jam)')
plt.ylabel('$y(t)$, (C)')
plt.show()
