
''' GA3 - Harmonic Oscillator

	Many simple molecular systems are modeled by a spring oscillator. They give us a nice
	differential equation to solve. Sometimes these models are quite accurate.

	A simple spring is stretched from its equillibrium length (x0) to some distance (xi),
	and then released. If the spring follows Hook's law (Equation 1)

	(1)		F = k(x - x0)

	We get an acceleration equation (Equation 2)

	(2)		a = -(k / m) * (x - x0)

	This equation can in fact be solved analytically; however, it involves a guess and 
	check relationship. We can express the energy as (Equation 3)

	(3)		E_total = E_kinetic + E_spring + E_gravitational

	(4)		E = (1/2)mv**2 + (1/2)k(x - x0)**2 + mgx

	If we take a numerical approach, all we need ins the acceleration equation (Equation 5)

	(5)		a(t) = -(k/m) x**2
'''

import matplotlib.pyplot as plt 
import numpy as np 

# Set up a "Control Panel".
k 	=	10		# Spring Constant (N/m) 
m 	= 	1		# Mass (kg)
x0 	= 	0.25	# Initial Position (m)
v0 	= 	0		# Initial Velocity (m/s)
dt 	= 	0.1		# Numerical Time-Delta (s)

def acceleration(x, k, m):
	''' Returns acceleration of a simple harmonic oscillator based on position

		Uses the equation:

				a(t) = - (k/m) x**2

		Args:
			x (float):	displacement, downwards positive (m)
			k (float):	spring constant (N/m)
			m (float):	mass (kg)

		Returns:
			float:	acceleration, downwards positive (m/s**2)
	'''

	return -1 * (k/m) * x


def euler_method(t0, x0, v0, k, m, tf, dt, modified=False, verbose=False):
	''' Returns t, x, v, and a lists for Modified Euler Method

		Args:
			t0 (float):	initial time (s)
			tf (float): final time (s)
			dt (float): time step (s)
			x0 (float): initial displacement, downwards positive (m)
			v0 (float): intiial velocity, downwards positive (m/s)
			k (float):	spring constant (N/m)
			m (float):	mass (kg)

			modified (bool):	turns on modified euler method.
			verbose (bool):		turns on printing of each time-step.

		Returns:
			float (list): list of times (s)			
			float (list): list of positions, downwards positive (m)
			float (list): list of velocities, downwards positive (m/s)
			float (list): list of acceleration, downwards positive (m/s**2)
	'''

	t = t0
	x = x0
	v = v0
	a = acceleration(x, k, m)

	t_num = [t]
	x_num = [x]
	v_num = [v]
	a_num = [a]

	while t < tf:
		if verbose: print('{:.3f} {:.3f} {:.3f} {:.3f}'.format(t, x, v, a))

		a = acceleration(x, k, m)
		t += dt

		if modified:
			v += dt * a
			x += dt * v
		else:
			x += dt * v
			v += dt * a

		t_num.append(t)
		x_num.append(x)
		v_num.append(v)
		a_num.append(a)

	return t_num, x_num, v_num, a_num

def oscillator_period(m, k):
	''' Return the period, T, of a simple harmonic oscillator.

	Uses:

		T = 2 * pi * sqrt(m / k)

	Args:
		m (float):	mass (kg)
		k (float):	spring constant (N/m)

	Returns:
		float:	period (s)

	'''

	return 2 * np.pi * np.sqrt(m / k)

tf = 50

t, x_simple, _, _   = euler_method(t0=0, tf=tf, x0=x0, v0=v0, k=k, m=m, dt=0.01, modified=False)
t, x_modified, _, _ = euler_method(t0=0, tf=tf, x0=x0, v0=v0, k=k, m=m, dt=0.01, modified=True)


plt.plot(t, x_simple, linestyle='-', color='black', linewidth=2)
plt.plot(t, x_modified, linestyle='-', color='black', linewidth=3)

i = 0
while i * oscillator_period(m, k) < tf:
	plt.axvline(i * oscillator_period(m, k), color='black', linewidth=1, linestyle='--')
	i += 1

plt.axhline(0.25 , linewidth=1, linestyle='--', color='black')
plt.axhline(-0.25, linewidth=1, linestyle='--', color='black')
plt.axhline(0, linewidth=1, linestyle='-', color='black')

plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')

plt.show()



