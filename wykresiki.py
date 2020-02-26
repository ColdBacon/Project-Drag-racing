import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint
from itertools import count


#co jesli nie podamy wszystkich wartosci

# for storing the results
vs1 = [0]
vs2 = [0]
# sps = np.zeros(nsteps)
dst1 = [0]
dst2 = [0]

slope = float(sys.argv[1]) #nachylenie 0.4
meta = float(sys.argv[2])  #maksymalny dystans 402
rho = 1.225 #rho = gestosc powietrza(kg/m^3)
tf = 60.0   # maksymalny czas symulacji

Cd1 = float(sys.argv[7])  #wspolczynnik oporu 0.29
Cd2 = float(sys.argv[8])
A1 = float(sys.argv[9]) #pole powierzchni czolowej 0.65
A2 = float(sys.argv[10])
moc1 = float(sys.argv[3])  #moc silnika [W] 100000
moc2 = float(sys.argv[4]) #90000
load1 = float(sys.argv[5])  # kg 1200
load2 = float(sys.argv[6])  # kg 1000

v01 = 0.0
v02 = 0.0

def vehicle(v, t, load, Cd, rho, A, moc):
    # inputs
    #  v    = vehicle velocity (m/s)
    #  t    = time (sec)
    # Cd = 0.24    Cd = drag coefficient
    # rho = 1.225   rho = air density (kg/m^3)
    # A = 5.0       A = cross-sectional area (m^2)
    # Fp = 5000       Fp = sila cigau samochodu
    # calculate derivative of the velocity
    if v<1:
        mocnyful=moc
    else:
        mocnyful=moc/v
    dv_dt = (mocnyful - 0.5 * rho * Cd * A * v ** 2 - load * 10 * slope) / load
    return dv_dt

delta_t = 0.1  # how long is each time step?
nsteps = int(tf / delta_t + 1)
print(nsteps)
ts =[0]
index = count()
i=0
next(index)

def animate(i):
    if(len(dst1)>0):
        if dst1[-1] < meta and dst2[-1] < meta:
            v1 = odeint(vehicle, vs1[-1], [0, delta_t], args=(load1, Cd1, rho, A1, moc1))
            v2 = odeint(vehicle, vs2[-1], [0, delta_t], args=(load2, Cd2, rho, A2, moc2))
            v01 = v1[-1]
            v02 = v2[-1]
            vs1.append(v01)
            vs2.append(v02)
            dst1.append(dst1[-1] + v01 * delta_t)
            dst2.append(dst2[-1] + v02 * delta_t)
            ts.append(next(index)*delta_t)
    else:
        dst1.append(0)
        dst2.append(0)
        v1 = odeint(vehicle, 0, [0, delta_t], args=(load1, Cd1, rho, A1, moc1))
        v2 = odeint(vehicle, 0, [0, delta_t], args=(load2, Cd2, rho, A2, moc2))
        ts.append(next(index)*delta_t)
    plt.subplot(2, 1, 1)
    plt.plot(ts, vs1, 'b-', linewidth=3)
    plt.plot(ts, vs2, 'k--', linewidth=2)
    plt.ylabel('Velocity (m/s)')
    plt.legend(['Velocity1', 'Velocity2'], loc=2)
    plt.subplot(2, 1, 2)
    plt.plot(ts, dst1, 'b--', linewidth=3)
    plt.plot(ts, dst2, 'k--', linewidth=3)
    plt.ylabel('Distance (m)')
    plt.legend(['Distance1', 'Distance2'], loc=2)

ani = FuncAnimation(plt.gcf(),animate,interval=100)

plt.show()
