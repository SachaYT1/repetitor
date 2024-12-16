import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.8  # acceleration due to gravity (m/s^2)
h = 20  # initial height (m)
v0 = 7.07  # initial horizontal velocity (m/s)

# Time of fall
t_fall = np.sqrt(2 * h / g)

# Generate time array
t = np.linspace(0, t_fall, 100)

# Calculate vertical velocity and position
v_y = g * t
y = h - 0.5 * g * t**2

# Calculate horizontal position
x = v0 * t

# Plot the motion
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.xlabel('Horizontal position (m)')
plt.ylabel('Vertical position (m)')
plt.title('Ball motion')
plt.grid(True)
plt.show()