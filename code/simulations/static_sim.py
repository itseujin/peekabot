# Period test with a = 0
# Applying equations of motion to the test in code

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
r = 1.0
dt = 0.001    # time step of 0.001
a = 0.0       # No acceleration of cart for now

# theta_d means first derivative with respect to time
# theta_dd means second derivative with respect to time

angle = int(input("Initial angle measured from upright: "))
theta = np.pi - np.radians(angle)
theta_d = 0.0
t = 0.0

# Keeping track of period and for graphing
times, angles, crossings = [], [], []

while t < 20:
    theta_dd = (a*np.cos(np.radians(angle)) + g*np.sin(np.radians(angle)))/r
    theta_d += theta_dd * dt
    prev = theta
    theta += theta_d * dt
    t += dt
    if prev < np.pi <= theta:    # just passed bottom
        crossings.append(t)      # append current time when passing bottom
    times.append(t)
    angles.append(np.degrees(theta))

# Checking period and graphing
print(f"Measured period: {np.mean(np.diff(crossings))}s")
print(f"Small-angle formula: {2*np.pi*np.sqrt(r/g)}s")

plt.plot(times, angles)
plt.xlabel("time (s)")
plt.ylabel("θ from upright (degrees)")
plt.grid(True)
plt.show()