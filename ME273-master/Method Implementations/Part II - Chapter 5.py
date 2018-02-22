from matplotlib import pyplot as plt 
import numpy as np

def func(g, m, c, t):
	return (g * m / c) * (1 - np.exp(-1 * (c / m) * t))

time = np.linspace(0, 60, 1e6)
velocity = func(g=9.81, m=75, c=20, t=time)

plt.plot(time, velocity)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()