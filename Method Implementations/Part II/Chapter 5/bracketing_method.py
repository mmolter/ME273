'''

	Bracking Methods

	These methods exploit the sign change that occurs at a root.

'''

''' Problem 1:
f
	Use the graphical approach to determine the drag coefficient
	c, needed for a parachutist of mass m = 68.1 kg to have a 
	velocity of 40 m/s after falling for time t = 10 s. Note, 
	the acceleration due to gravity, g, is 9.81 m/s/s
'''

import numpy as np
from matplotlib import pyplot as plt

import unittest

def g(x):
	return np.cos(x)

def ea(old, new):
	return abs((new - old) / old)

def bisect(func, xl, xu, et=0.001, 
	max_iterations=int(1e6), verbose=False):

	for i in range(max_iterations):
		xr = (xl + xu) / 2

		if verbose:
			print(('xl: {xl:<5.4f}\txu: {xu:<5.4f}\t'
				   'xr: {xr:<5.4f}\tea: {ea:<5.4f}\t'
				   'func(xl): {fxl:<5.4f}\t'
				   'func(xu): {fxu:<5.4f}').format(
					xu=xu, xl=xl, xr=xr, 
					ea=ea(old=xr, new=(xl+xu)/2), 
					fxl=func(xl), fxu=func(xu)))

		if func(xl) * func(xr) < 0:
			xu = xr
		elif func(xl) * func(xr) > 0:
			xl = xr
		else:
			return xr

		if ea(old=xr, new=(xl + xu) / 2) < et:
			return (xl + xu) / 2

	else:
		print('Failed to find root in {} iterations.'.format(max_iterations))

def false_position(func, xl, xu, et=0.001):
	while True:
		fl = func(xl)
		fu = func(xu)

		xr = xu - fu * (xl - xu) / (fl - fu)
		fr = func(xr)

		if fl * fr > 0:
			xl = xr
		elif fu * fr > 0:
			xu = xr
		else:
			print('Error! Sign mismatch.')
			return 0

		if ea(old=xr, new=xu - fu * (xl - xu) / (fl - fu)) < et:
			return (xl + xu) / 2	

class TestBracketingMethods(unittest.TestCase):
	def test_bisect(self):
		self.assertAlmostEqual(bisect(np.cos, xl=0, xu=3), np.pi / 2, places=2)
		self.assertAlmostEqual(bisect(np.sin, xl=1, xu=5), np.pi, places=2)
		self.assertAlmostEqual(bisect(lambda x: 2 ** x - 5, xl=0, xu=3), 2.322, places=2)

	def test_false_position(self):
		self.assertAlmostEqual(false_position(np.cos, xl=0, xu=3), np.pi / 2, places=2)
		self.assertAlmostEqual(false_position(np.sin, xl=1, xu=5), np.pi, places=2)
		self.assertAlmostEqual(false_position(lambda x: 2 ** x - 5, xl=0, xu=3), 2.322, places=2)

if __name__ == '__main__':
	unittest.main()


