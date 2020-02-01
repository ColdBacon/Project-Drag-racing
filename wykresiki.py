import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

slope = 0.4 #nachylenie
meta = 402  #maksymalny dystans
rho = 1.225 #rho = gestosc powietrza(kg/m^3)
tf = 60.0   # maksymalny czas symulacji
# animate plots?
animate = True  # True / False
Cd1 = 0.29  #wspolczynnik oporu
Cd2 = 0.29
A1 = 0.65    #pole powierzchni czolowej
A2 = 0.65
moc1 = 100000  #moc silnika [W]
moc2 = 90000
load1 = 1200.0  # kg
load2 = 1000.0  # kg


# define model
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
ts = np.linspace(0, tf, nsteps)  # linearly spaced time vector

# simulate step test operation
# passenger(s) + cargo load
load = 800.0  # kg
# velocity initial condition
v01 = 0.0
v02 = 0.0
# set point
# sp = 25.0
# for storing the results
vs1 = np.zeros(nsteps)
vs2 = np.zeros(nsteps)
# sps = np.zeros(nsteps)
dst1 = np.zeros(nsteps)
dst2 = np.zeros(nsteps)

plt.figure(1, figsize=(5, 4))
if animate:
    plt.ion()
    plt.show()

i = 0
u = 0
# simulate with ODEINT
while True:
    if dst1[i] < meta and dst2[i] < meta:
        v1 = odeint(vehicle, v01, [0, delta_t], args=(load1, Cd1, rho, A1, moc1))
        v2 = odeint(vehicle, v02, [0, delta_t], args=(load2, Cd2, rho, A2, moc2))
        if v1[-1] < 0:
            v1[-1] = 0
        if v2[-1] < 0:
            v2[-1] = 0
        if v1[-1] == 0 and v2[-1] == 0:
            print("Oba samochody sie zatrzymaly")
            break
        v01 = v1[-1]  # take the last value
        v02 = v2[-1]
        vs1[i + 1] = v01  # store the velocity for plotting
        vs2[i + 1] = v02
        # sps[i+1] = sp
        dst1[i + 1] = dst1[i] + v01 * delta_t
        dst2[i + 1] = dst2[i] + v02 * delta_t

        # plot results
        # if animate:
        plt.clf()  # clf=wyczysc wszystko
        plt.subplot(2, 1, 1)
        plt.plot(ts[0:i + 1], vs1[0:i + 1], 'b-', linewidth=3)
        plt.plot(ts[0:i + 1], vs2[0:i + 1], 'k--', linewidth=2)
        plt.ylabel('Velocity (m/s)')
        plt.legend(['Velocity1', 'Velocity2'], loc=2)
        plt.subplot(2, 1, 2)
        plt.plot(ts[0:i + 1], dst1[0:i + 1], 'b--', linewidth=3)
        plt.plot(ts[0:i + 1], dst2[0:i + 1], 'k--', linewidth=3)
        plt.ylabel('Distance (m)')
        plt.legend(['Distance1', 'Distance2'], loc=2)
        plt.pause(0.01)
    else:
        if dst1[i] > dst2[i]:
            print("Wygral 1szy")
            print(dst1[i], vs1[i], i)
        else:
            print("Wygral drugi")
            print(dst2[i], vs2[i], i)
        break
    i += 1

if not animate:
    # plot results
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
    plt.show()
