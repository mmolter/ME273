import numpy as np
import matplotlib.pyplot as plt

''' Assignment questions:

    Exercise 1: Computational model of a falling sphere with air resistance

    Produce a working computational model in MATLAB (or OCTAVE, or in another
    programming language of your choice) of a sphere that has been dropped from
    rest from a very tall building using the simple Euler method. Assume that the
    sphere will move entirely in one dimension, and that it is subject to the constant
    gravitational force near Earth's surface and to a drag for proportional to the
    square of the sphere's instantaneous speed.

    Exercise 2: Accuracy of computational model: velocity v. time

    Since the computation approach is based on an approximation, it is important to
    determine jsut how small delta t should be for the approximation to accurately 
    solve the 1-D air resistance problem. Make a comparison between the time dependence
    of the velocity predicted by the computational model, and that predicted by the
    exact result.

    Use parameters that describe a 16 lbs bowling ball (you should look up the
    diamter, and convert to meters), and let it fall a distance equivalent ot the 
    height of the Sears, oops - Willis, tower (440 m). Assume the ball is initially
    at rest. Use a value of 0.5 for the drag coefficient, and the density of air near
    sea level. What value of delta t do you deem to be sufficiently small for the
    computational model to be accurate? Explain how you arrived at this value.

    Exercise 3: accuracy of the computational model: position v. time

    Carry out the same comparison (computational v. exact analytical solution) for
    the bowling ball's posistion as a function of time.

    Assume the bowling ball is falling the same distance of 440 m. Do you find the 
    same value of delta t as you found for the velocity comparison in exersise 2 to
    be acceptable for the poistion comparison?

    Exercise 4: position and velocity of dropped bowling ball

    Produce plots of the bowling ball's velocity and vertical position as functions
    of time from teh results of the computational model, using the parameters from the
    previous exercises and the value of delta t (determined in exercises 2 and 3) that 
    produces a tolerably accurate compuational solution. Has the bowling ball reached
    its terminal velocity by the time it hits the ground? Use your model to predict the
    time required for the bowling ball to fall the full 440 meters to the ground.

    Exercise 5: position and velocity of a dropped mystery sphere

    Repeat exercise 4 for a different sphere (of your choice). How long does it take to
    travel the 440 meters to the ground, and has it reached its terminal velocity upon
    impact?
'''

def acceleration(vel, area, mass, rho=1.225, g=9.80665, D=0.5):
  ''' Return the acceleration of a body in free-fall accounting for drag.
  
  Uses the equation:
  
    a = g - [(D * rho * A) / (2 * m)](v**2)
  
  Args:
    vel (float):    the current velocity of the object m/s
    area (float):   the cross-sectional area of the object in m**2
    mass (float):   the mass of the object in kg
    rho (float):    the density of air in kg/m**3 (default 1.225 kg/m**3)
    g (float):      the acceleration due to gravity in m/s**2 (defautl 9.80665 m/s**2)
    D (float):      the drag coefficient (default to 0.5 for a sphere)
    
      Other common shapes (https://en.wikipedia.org/wiki/Drag_coefficient):
        0.47 -- Sphere
        0.42 -- Half Sphere
        0.50 -- Cone
        1.05 -- Cube
        0.80 -- Diamond
        0.82 -- Long Cylinder
        1.15 -- Short Cylinder
        0.04 -- Airfoil
        0.09 -- Half Airfoil
        0.25 -- Toyota Prius (goo.gl/uagxXZ)
        
  Returns:
    float:  the acceleration in m/s**2 for the body.
  '''
  
  return -1 * (g - ((D * rho * area) / (2 * mass))*(vel**2))
  
def velocity_exact(t, area, mass, rho=1.225, g=9.80665, D=0.5):
  ''' Returns the analytical velocity of a body in free-fall at time t.
  
  Uses the equation:
  
    v = sqrt((2 * m * g) / (D * rho * A)) * tanh(sqrt((D * rho * A * g) / (2 * m)) * t)
  
  Args:
    t (float):      the current time in seconds
    area (float):   the cross-sectional area of the object in m**2
    mass (float):   the mass of the object in kg
    rho (float):    the density of air in kg/m**3 (default 1.225 kg/m**3)
    g (float):      the acceleration due to gravity in m/s**2 (defautl 9.80665 m/s**2)
    D (float):      the drag coefficient (default to 0.5 for a sphere)
        
  Returns:
    float:  the velocity in m/s for the body.
  '''
  
  return -1 * np.sqrt((2 * mass * g) / (D * rho * area)) * np.tanh(np.sqrt((D * rho * area * g) / (2 * mass)) * t)
  
def position_exact(t, x0, area, mass, rho=1.225, g=9.80665, D=0.5):
  ''' Returns the analytical position of a body in free-fall at time t.
  
  Uses the equation:
  
    v = ((2 * m * g) / (D * rho * A)) * ln[cosh(sqrt((D * rho * A * g) / (2 * m)) * t)]
  
  Args:
    t (float):      the current time in seconds
    area (float):   the cross-sectional area of the object in m**2
    mass (float):   the mass of the object in kg
    rho (float):    the density of air in kg/m**3 (default 1.225 kg/m**3)
    g (float):      the acceleration due to gravity in m/s**2 (defautl 9.80665 m/s**2)
    D (float):      the drag coefficient (default to 0.5 for a sphere)
        
  Returns:
    float:  the position in m for the body.
  '''
  
  return x0 - ((2 * mass) / (D * rho * area)) * np.log(np.cosh(np.sqrt((D * rho * area * g) / (2 * mass)) * t))

def euler_projectile(mass, area, x0=0, xf=0, v0=0, dt=0.01, **kwargs):
    ''' Returns time, position, velocity and acceleration of a body in free-fall with drag.

    Uses a Euler approximation with a time-detla, dt, to numerically approximate the motion
    of a body in free-fall under the influence of gravity and drag.

    Args:
        mass (float):   the mass of the object in kg
        area (float):   the cross-sectional area of the object in m**2
        x0 (float):     the intial position of the object in m
        v0 (float):     the initial velocity of the object in m/s
        dt (float):     the time-step for the simulation in s
        **kwargs:		keyword arguments for modifying accelertaion function.

    Returns:
        list (float): time stamps
        list (float): positions
        list (float): velocities
        list (float): accelerations

    '''

    t = 0
    x = x0
    v = v0
    a = acceleration(v0, area=area, mass=mass, **kwargs)

    t_num = [t]
    x_num = [x]
    v_num = [v]
    a_num = [a]

    while x >= xf:
        t += dt
        x += dt * v
        v += dt * a
        a = acceleration(v, area=area, mass=mass, **kwargs)

        t_num.append(t)
        x_num.append(x)
        v_num.append(v)
        a_num.append(a)

    return t_num, x_num, v_num, a_num

def exact_projectile(times, mass, area, x0=0, **kwargs):
    ''' Returns time, position, velocity and acceleration of a body in free-fall with drag for a given list of times.

    Uses analytical solutions to free-fall with drage ODEs to provide exact time, position,
    velocity, and acceleration arrays for a given timestep.

    Args:
        mass (float):   the mass of the object in kg
        area (float):   the cross-sectional area of the object in m**2
        x0 (float):     the intial position of the object in m
        v0 (float):     the initial velocity of the object in m/s
        dt (float):     the time-step for the simulation in s
        **kwargs:		keyword arguments for modifying accelertaion function.

    Returns:
        list (float): time stamps
        list (float): positions
        list (float): velocities
        list (float): accelerations

    '''

    t_exact = times
    x_exact = position_exact(np.asarray(times), x0, area, mass, **kwargs)
    v_exact = velocity_exact(np.asarray(times), area, mass, **kwargs)
    a_exact =   acceleration(np.asarray(v_exact), area, mass, **kwargs)

    return t_exact, x_exact, v_exact, a_exact

def absolute_error(approx, exact):
    ''' Returns absolute error between two lists.

    Args:
        approx (list):  the list of numerical values.
        exact (list):   the list of exact values.

    Returns:
        list (float):   list of absolute errors
    '''

    return [abs(a - e) for a, e in zip(approx, exact)]

def relative_error(approx, exact):
    ''' Returns relative error between two lists.

    Args:
        approx (list):  the list of numerical values.
        exact (list):   the list of exact values.

    Returns:
        list (float):   list of relative errors
    '''

    return [abs(a - e) / e if e != 0 else 0 for a, e in zip(approx, exact)]


if __name__ == '__main__':

  ''' Exercise 1: Compatational Model of a Falling Sphere w/Air Resistance
        
          (1) Implement model based on Euler approximation
          
       Model: Typical Bowling Ball (Serway, 1999)
       
        Mass:   8 kg
        Radius: 0.012 m
       
       Serway, Raymond. Physics for Scientists and Engineers, with Modern Physics.
          Brooks Publishing Company; 5th Edition, 1998: 338.

  '''
  radius = 0.012
  area = np.pi * radius**2

  mass = 8

  h = 440

  dt = 0.001

  t_num, x_num, v_num, a_num = euler_projectile(mass=mass, area=area, x0=h, dt=dt)

  ''' Exercise 2: Accuracy of the Computational Model: Velocity v. Time
        
        (1)   Compare model to exact, analytical velocity while x < 440 m.
        (2a)  What delta-t is sufficently small?
        (2b)  How do you know?
          
      Exercise 3: Accuracy of the Computational Model: Position v. Time
      
        (1)   Compare model to exact, analytical position while x < 440 m.
        (2a)  What delta-t is sufficiently small?
        (2b)  How does this compare the required delta-t for the velocity approximation?
  '''

  # Find the exact, analytical velocity and position for the time steps we used in our model.
  t_exact, x_exact, v_exact, a_exact = exact_projectile(times=t_num, mass=mass, area=area, x0=h)
  
  # Compare the worst-case error for both approximations
  v_rel_error = max(relative_error(v_num, v_exact))
  x_rel_error = max(relative_error(x_num, x_exact))

  v_abs_error = max(absolute_error(v_num, v_exact))
  x_abs_error = max(absolute_error(v_num, v_exact))
  
  # Print results to console
  print('For t-delta {} (s):'.format(dt))
  print('Worst-case Velocity Error:\t{:.3f} (m/s)'.format(v_abs_error))
  print('Worst-case Position Error:\t{:.3f} (m)'.format(x_abs_error))

  ''' Exercise 4: Position and Velocity of a Dropped Bowling Ball
        
        (1)   Plot your compuational models for position and velocity.
        (2)   Did the ball reach terminal velocity?
        (3)   How long does it take to hit the ground?
  '''
  
  f, (ax, av, aa) = plt.subplots(3, sharex=True)
  
  ax.plot(t_num, x_num, color='black', linestyle='-')
  ax.plot(t_exact, x_exact, color='black', linestyle='--')

  av.plot(t_num, v_num, color='black', linestyle='-')
  av.plot(t_exact, v_exact, color='black', linestyle='--')

  aa.plot(t_num, a_num, color='black', linestyle='-')
  aa.plot(t_exact, a_exact, color='black', linestyle='--')
  
  ax.set_ylabel('Position ($m$)')
  av.set_ylabel('Velocity ($m/s$)')
  aa.set_ylabel('Acceleration ($m/s^2$)')
  
  aa.set_xlabel('Time ($s$)')
  
  plt.show()
  
  # Find the terminal velocity
  v_terminal = velocity_exact(1e6, area, mass)
  
  # Find how close we were to terminal velocity at x == 0 m
  per_of_term = abs(min(v_num)) / abs(v_terminal)
  
  print('At x = 0 m, the ball reached {speed:.1f} m/s or {per:.1f} % of terminal velocity'.format(speed=min(v_num),
                                                                                              per=per_of_term * 100))
  TOF_num = max(t_num)
  TOF_exact = 0

  print('According to the model, the object fell for {:.2f} (s).'.format(TOF_num))


  ''' Exercise 5: Position and Velocity of a Dropped Mystery Sphere

  		(1) Plot position, velocity, and acceleration
  		(2) How long does it take to travel 440 (m)?
  		(3) Has it reached terminal velocity?
  
  '''

  # Object: 'Toyota Prius'
  m = 1325
  D = 0.25
  A = 1.470 * 1.760 
  h = 440


  dt = 0.01

  t_num, x_num, v_num, a_num = euler_projectile(mass=m, area=A, x0=h, dt=dt, D=D)

  print()
  print('A Toyota Prius (Gen 4), weighing 1325 kg, with a frontal cross-section of',
  	    '1,470 mm x 1,760 mm, and a slick Cd of 0.25 is dropped from the top of the',
  	    'Sears Tower (440 m)')

  print('It falls for a total of {:.2f} (s)'.format(max(t_num)))

  terminal_velocity = abs(velocity_exact(t=1e10, area=A, mass=m, D=D))
  percent_of_term = abs(min(v_num)) / terminal_velocity * 100

  print('and reaches {:.0f} mph or {:.1f} % of its terminal velocity ({:.0f} mph).'.format(abs(min(v_num)) * 2.23694, percent_of_term, terminal_velocity * 2.23694))
  print('Not a single tear is shed.')