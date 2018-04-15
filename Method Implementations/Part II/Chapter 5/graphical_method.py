'''

	Bracking Methods

	These methods exploit the sign change that occurs at a root.

'''

''' Problem 1:

	Use the graphical approach to determine the drag coefficient
	c, needed for a parachutist of mass m = 68.1 kg to have a 
	velocity of 40 m/s after falling for time t = 10 s. Note, 
	the acceleration due to gravity, g, is 9.81 m/s/s
'''

import numpy as np
from matplotlib import pyplot as plt

res = 500

def f(g, m , v, c, t):
	return (g * m / c) * (1 - np.exp((-1 * c / m) * t)) - v

def g(x):
	return np.sin(10 * x) + np.cos(3 * x)

f, axarr = plt.subplots(3, facecolor='#cceefb')

x = np.linspace(0, 5, res)
axarr[0].plot(x, g(x), c='black')
axarr[0].axhline(y=0, c='black', linewidth='0.5')
axarr[0].set_axis_bgcolor('white')
axarr[0].tick_params(direction='in')

x = np.linspace(3, 5, res)
axarr[1].plot(x, g(x), c='black')
axarr[1].axhline(y=0, c='black', linewidth='0.5')
axarr[1].tick_params(direction='in')

x = np.linspace(4.2, 4.3, res)
axarr[2].plot(x, g(x), c='black')
axarr[2].axhline(y=0, c='black', linewidth='0.5')
axarr[2].tick_params(direction='in')


f = plt.xlabel('x')
f = plt.ylabel('g(x)')
plt.show()