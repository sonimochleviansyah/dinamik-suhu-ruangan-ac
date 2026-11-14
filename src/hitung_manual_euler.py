import numpy as np
from scipy.integrate import odeint

T_out, tau, k = 32.0, 2.0, 0.07
h = 0.5
t = np.arange(0, 3.0 + h, h)
rows = []
T = 30.0
for ti in t:
    u = 100.0 if 2.0 <= ti < 7.0 else 0.0
    f = (T_out - T) / tau - k * u
    rows.append((ti, u, T, f))
    T = T + h * f

# solusi analitik per segmen
def analitik(tt):
    if tt <= 2:
        return T_out + (30.0 - T_out) * np.exp(-tt / tau)
    T2 = T_out + (30.0 - T_out) * np.exp(-2 / tau)
    Tss = T_out - k * 100 * tau
    return Tss + (T2 - Tss) * np.exp(-(tt - 2) / tau)

def f_ode(T, t):
    u = 100.0 if 2.0 <= t <= 7.0 else 0.0
    return (T_out - T) / tau - k * u
od = odeint(f_ode, 30.0, t, tcrit=[2.0])[:, 0]

print('t | u | T_euler | dT/dt | T_analitik | T_odeint | galat')
for (ti, u, Te, f), o in zip(rows, od):
    a = analitik(ti)
    print('%.1f | %3.0f | %.4f | %+.4f | %.4f | %.4f | %.4f' % (ti, u, Te, f, a, o, abs(Te - a)))
