import matplotlib.pyplot as plt
import numpy as np

def runga_kutta(func, yl, xl, xu, h):
	''' For a function dy/dx = func(x, y), returns a list of x + h, y values. '''
	y = yl
	x = xl

	xs = [xl]
	ys = [yl]
	while x < xu:
		k1 = func(x + 0.0*h, y + 0.0*h)
		k2 = func(x + 0.5*h, y + 0.5*k1*h)
		k3 = func(x + 0.5*h, y + 0.5*k2*h)
		k4 = func(x + 1.0*h, y + 1.0*k3*h)

		y += (1/6)*(k1 + 2*k2 + 2*k3 + k4)*h
		x += h

		xs.append(x)
		ys.append(y)

	return xs, ys
