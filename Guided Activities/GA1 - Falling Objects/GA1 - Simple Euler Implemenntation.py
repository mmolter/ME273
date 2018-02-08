import numpy as np
import matplotlib.pyplot as plt

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
  
  
  
