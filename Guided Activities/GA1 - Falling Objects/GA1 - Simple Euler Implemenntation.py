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
  pass
  
  
