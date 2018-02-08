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
''''

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
  
  return g - ((D * rho * area) / (2 * mass))*(vel**2)
  
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
  
  return np.sqrt((2 * m) / (D * rho * area)) * np.tanh(np.sqrt((D * rho * A * g) / (2 * m)) * t)
  
def position_exact(t, area, mass, rho=1.225, g=9.80665, D=0.5):
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
  
  return ((2 * m) / (D * rho * area)) * np.ln(np.cosh(np.sqrt((D * rho * A * g) / (2 * m)) * t))
  

if __name__ == '__main__':
  
  ''' Exercise 1: Deliverable Requirements
        
          (1) Implement model based on Euler approximation
          
       Model: Typical Bowling Ball (Serway, 1999)
       
        Mass:   8 kg
        Radius: 0.012 m
       
       Serway, Raymond. Physics for Scientists and Engineers, with Modern Physics.
          Brooks Publishing Company; 5th Edition, 1998: 338.

  '''
  radius = 0.012
  mass = 8
  area = np.pi * radius**2
  
  t = 0
  x = 440
  v = 0
  a = acceleration(v, area, mass)
  
  dt = 0.01
  tmax = 30
  
  t_num = [t]
  x_num = [x]
  v_num = [v]
  a_num = [a]
  
  while t < tmax:
    a = acceleration(v, area, mass)
    
    t += dt 
    x += dt * v
    v += dt * a
    
    t_num.append(t)
    x_num.append(x)
    v_num.append(v)
    a_num.append(a)
    
  ''' Exercise 2: Deliverable Requirements
        
        (1)   Compare model to exact, analytical velocity while x < 440 m.
        (2a)  What delta-t is sufficently small?
        (2b)  How do you know?
          
      Exercise 3: Deliverable Requirements
      
        (1)   Compare model to exact, analytical position while x < 440 m.
        (2a)  What delta-t is sufficiently small?
        (2b)  How does this compare the required delta-t for the velocity approximation?
  '''

  # Find the exact, analytical velocity and position for the time steps we used in our model.
  t_exact = np.asarray(t_num)
  x_exact = position_exact(np.asarray(t_num), area, mass)
  v_exact = velocity_exact(np.asarray(t_num), area, mass)
  a_exact = acceleartion(t_exact, area, mass)

  # Filter for points where x < 440 m
  x_num = [x for x in x_num if x >= 0]
  t_num = [t for t, x in zip(t_num, x_num) if x >= 0]
  v_num = [v for x, v in zip(x_num, v_num) if x >= 0]
  a_num = [a for x, a in zip(x_num, a_num) if x >= 0]
  
  x_exact = [x for x in x_exact if x >= 0]
  t_exact = [t for t, x in zip(t_exact, x_exact) if x >= 0]
  v_exact = [v for x, v in zip(x_exact, v_exact) if x >= 0]
  a_exact = [a for x, a in zip(x_exact, a_exact) if x >= 0]
  
  # Compare the worst-case error for both approximations
  v_error = max(abs((v_n - v_e) / v_e) for v_n, v_e in zip(v_num, v_exact))
  x_error = max(abs((x_n - x_e) / x_e) for x_n, x_e in zip(x_num, x_exact))
  
  # Print results to console
  print('For t-delta {} (s):'.format(dt))
  print('Worst-case Velocity Error:\t{:.1<3} %'.format(v_error))
  print('Worst-case Position Error:\t{:.1<3} %'.format(x_error))
  
  ''' Exercise 4: Deliverable Requirements
        
        (1)   Plot your compuational models for position and velocity.
        (2)   Did the ball reach terminal velocity?
        (3)   How long does it take to hit the ground?
  '''
  
  f, (ax, av, aa) = plt.subplots(3, sharex=True)
  
  ax.plot(t_num, x_num)
  av.plot(t_num, v_num)
  aa.plot(t_num, a_num)
  
  ax.ylabel('Position ($m$)')
  av.ylabel('Velocity ($m/s$)')
  aa.ylabel('Acceleration ($m/s^2$)')
  
  aa.xlabel('Time ($s$)')
  
  f.show()
  
  # Find the terminal velocity
  v_terminal = velocity_exact(t=np.inf, area, mass)
  
  # Find how close we were to terminal velocity at x == 0 m
  per_of_term = max(v_num) / v_terminal
  
  print('At x = 0 m, the ball reached {speed:.2f} or {per:.1f} % of terminal velocity'.format(speed=max(v_num),
                                                                                              per=per_of_term))
  
  
                
       
  
  
