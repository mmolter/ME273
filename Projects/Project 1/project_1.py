import matplotlib.pyplot as plt
import numpy as np

def drag(v, D, rho, A):
    ''' Return drag force on a projectile subject to air resistance.
        
        Returns a force vector in the opposite direction as the velocity
        vector with a magnitude determined by the drag equation below.

                    F_d = (D * rho * A) / 2 * v**2

        Args:
            
            v (np.array):       velocity vector 
            D (np.float64):     drag coefficient
            rho (np.float64):   air density (units)
            A (np.float64):     cross-sectional area (m**2)

        Returns:

            (np.array):         drag force vector 
    '''

    F_d = ((D * rho * A) / 2) * magnitude(v)**2
    
    return F_d * (-1) * unit_vector(v)

def unit_vector(x):
    ''' Return unit vector for vector x. 

        Args:

            x (np.array):   input vector

        Returns
            
            (np.array):     unit vector for x
    '''

    return x / magnitude(x)

def magnitude(x):
    ''' Return mangitude of vector x. 

        Args:

            x (np.array):   input vector

        Returns
            
            (np.float64):   magnitude of x 
    '''

    return np.sqrt(np.sum(x * x))

def air_density(y, rho0=1.2, c=6.5e-3, T0=300, alpha=2.5):
    ''' Return altitude dependent air density, rho.

        Derrived from thermodynamic calculations and remains
        a good approximation upt to 10 km (Roos, 2018).

        Uses:

            rho(y) = rho0 (1 - (cy/T0))**alpha

        Args:

            y (float):      altitude (m)
            rho (float):    air density as sea level (kg/m**3)
            c (float):      temperature fall (K/m)
            T0 (float):     temperature at sea level (K)
            alpha (float):  unknown?

        Returns:
            
            (float):        air density at altitude (kg/m**3)
    '''

    return rho0 * (1 - c * y / T0)**alpha


