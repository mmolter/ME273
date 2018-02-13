'''------------------------------------------------------------------------------

	Project: 	Projectile Calculator

	Author:		M. Molter	

	Date:		Tue., 6 Feb. 2018

	Desc:		A projectile calculator based on a Euler approximation of the 
				'free-fall with drag' formula. Users can change mass, air 
				density (rho), drag coefficent (D), or projectile radius by 
				editing acceleration(). 

				I am being 'un-pythonicly' verbose in my comments in order to
				make the program flow clear if python isn't your language of 
				choice...

--------------------------------------------------------------------------------'''

# Importing required packages
import matplotlib.pyplot as plt  	# Plotting
import matplotlib				 	# Plotting
import numpy as np 				 	# Numerical Methods

from collections import namedtuple 	# Abstract Python Containers

# Define a function with our chosen model of 'free-fall with drag'.
def acceleration(vel, d=0.5, rho=1.29, mass=0.625, gravity=9.81, radius=0.12):
	''' Return the acceleration for a body in free-fall with drag. '''

	area = np.pi * radius ** 2
	return gravity - ((d * rho * area) / (2.0 * mass)) * vel**2

# Create an abstract container for points along the curves.
Point = namedtuple('Point', ['t', 'x', 'v', 'a'])

# Create an initial and final point defining boundary conditions.
initial = Point(t=0, x=0, v=0, a=acceleration(0))
final   = Point(t=15, x=None, v=None, a=None)

# Create a list of points as we graph the curves.
points = [initial]

# Set the time step
dt = 0.01

t = initial.t
while t <= final.t:
	# Grab the last point we calculated, and
	# un-pack the tuple containing its values.
	t, x, v, a = points[-1]

	# Calculate the next point's values.
	a  = acceleration(vel=v)
	t += dt
	x += v * dt
	v += a * dt

	# Thow that new point in the list.
	points.append(Point(t, x, v, a))


# ------ Ploting Code --------------------------------------------------

# Create lists of just the times, positions,
#  velocities, and accelerations.
ts, xs, vs, aes = zip(*points)

# Set the global plot border to 1.1 pt.
matplotlib.rc('axes', linewidth=1.1)
plt.rcParams['savefig.dpi'] = 500

# Create three subplots.
f, (ax, av, aa) = plt.subplots(3, sharex=True)

# Set the parameters common to the three subplots.
for axis, ys in zip([ax, av, aa], [xs, vs, aes]):

	# Plot the data in black with 1 pt. linewidth.
	axis.plot(ts, ys, color='black', linewidth=1)

	# Set the major and minor ticks to inward.
	axis.tick_params(which='both', direction='in')

	# Turn on the horizontal and vertical grids.
	axis.grid(which='both')

# Give the plot a title.
ax.set_title('FREE FALL WITH DRAG', weight='heavy')

# Adjust the tick spacing for each of the subplots.
ax.yaxis.set_ticks(np.arange(0, ax.get_ylim()[1], 50))
av.yaxis.set_ticks(np.arange(0, av.get_ylim()[1], 5))
aa.yaxis.set_ticks(np.arange(0, aa.get_ylim()[1], 2.5))

# Label the y-axes.
ax.set_ylabel('Position ($m$)')
av.set_ylabel('Velocity ($m/s$)')
aa.set_ylabel('Acceleration ($m/s^2$)')

# Label the x-axis.
plt.xlabel('Time ($s$)')

# Display the plot.
plt.show()