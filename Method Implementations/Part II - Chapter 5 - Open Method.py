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

def g(x):
	return np.exp(-1 * x) - x

def ea(old, new):
	return abs((new - old) / old)

def simple_fixed_point(func, xo, et=0.001):
	x = func(xo) + xo
	while True:
		xi = func(x) + x

		if ea(old=x, new=xi) < et:
			return xi
		else:
			x = xi

def secant(func, xo, et=0.001, s=0.0001):
	x = xo - (s * func(xo)) / (func(xo + s) - func(xo))
	while True:
		print(x)
		xi = x - (s * func(x)) / (func(x + s) - func(x))

		if ea(old=x, new=xi) < et:
			return xi
		else:
			x = xi


print(secant(g, 0))


