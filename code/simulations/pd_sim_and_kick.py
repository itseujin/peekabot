import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
# small animation to visualise entire system
import time
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation

g = 9.81
r = 1.0
dt = 0.001    # time step of 0.001
a = 0.0       # No acceleration of cart for now

Kx, Kv = 1.0, 2.0

def controller(theta, theta_d, x, v):
    return -(Kp*theta + Kd*theta_d) + Kx*x + Kv*v   # addition of full-state feedback by introducing x and v

angle = int(input("Initial lean from upright: "))
position = int(input("Parking position of cart: "))

Kp = int(input("Kp Value: "))     # Implementing my equations for Kp and Kd, where Kd will be optimised for critically damped oscillations
Kd =  np.sqrt(4*r*(Kp-g))

theta = np.radians(angle)     # no more "pi - angle", this is now staring from upright direction
theta_d = 0.0
x, v, t = 0.0, 0.0, 0.0       # saving position and speed of cart as well

# Keeping track for the animation
times, thetas, xs = [], [], []

# Adding a boolean to check if it has been kicked ornot
kicked = False

# calculations and storing of position and data
while t < 20:

    a = controller(theta, theta_d, x-position, v)     # manipulate where the cart "parks"
    theta_dd = (a*np.cos(theta) + g*np.sin(theta))/r
    theta_d += theta_dd * dt
    theta += theta_d * dt

    v += a * dt
    x += v * dt
    t += dt

    if t >= 3.0 and not kicked:   # hard coded to apply a change in theta_d at 3 seconds in.
        theta_d += 2.0
        kicked = True

    xs.append(x)
    times.append(t)
    thetas.append(theta)


# Animation section for visualisation only, copied and adapted from the Internet
cart_w, cart_h = 0.4, 0.2

fig, ax = plt.subplots(figsize=(8, 5))
ax.set_aspect("equal")
ax.set_ylim(-0.2, 1.4)
ax.axhline(0, color="grey")                                   # ground
cart = Rectangle((0, 0), cart_w, cart_h, color="tab:blue")
ax.add_patch(cart)
pole, = ax.plot([], [], lw=6, color="tab:orange", solid_capstyle="round")
clock = ax.text(0.02, 0.92, "", transform=ax.transAxes)      # on-screen timer

start = None
def update(_):
    global start
    if start is None:
        start = time.perf_counter()
    k = min(int((time.perf_counter() - start) / dt), len(thetas) - 1)  # sim step matching real time
    x, th = xs[k], thetas[k]
    tip_x = x - r * np.sin(th)          # minus: θ > 0 = leaning left
    tip_y = cart_h + r * np.cos(th)
    cart.set_xy((x - cart_w / 2, 0))
    pole.set_data([x, tip_x], [cart_h, tip_y])
    ax.set_xlim(x - 1.5, x + 1.5)       # camera follows the cart
    clock.set_text(f"t = {k * dt:.2f} s")
    return cart, pole, clock

anim = FuncAnimation(fig, update, interval=20, blit=False, cache_frame_data=False)
plt.show()