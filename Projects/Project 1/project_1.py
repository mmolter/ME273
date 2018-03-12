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

    return (rhi0 * (1 - c * y / T0))**alpha

def euler_method(acceleration, t0, tf, dt, x0=0, v0=0, modified=False, **kwargs):
    ''' Returns t, x, v, and a arrays for Euler Method

    Args:
        acceleration (func):    acceleration function **

        t0 (float):             initial time (s)
        tf (float):             final time (s)
        dt (float):             time step (s)
        
        x0 (np.array):          initial displacement (m)
        v0 (np.array):          initial velocity (m/s)
        **kwargs:               any additional parameters required for
                                    acceleration function.

    Returns:
        np.float64 (np.array):  list of times (s)
        np.float64 (np.array):  list positions (m)
        np.float64 (np.array):  list velocities (m/s)
        np.float64 (np.array):  list accelerations (m/s**2)
    '''

    t = np.arange(t0, tf, dt, dtype=np.float64)

    points = t.size
    dimensions, = x0.shape

    x = np.empty([points, dimesnions])
    v = np.empty([points, dimesnions])
    a = np.empty([points, dimesnions])

    x[0] = x0
    v[0] = v0
    a[0] = acceleration(x0, v0, **kwargs)

    for i in range(1, points):
        a[i] = acceleration(x[i-1], v[i-1], **kwargs)

        if modified:
            v[i] = v[i-1] + dt * a[i]
            x[i] = x[i-1] + dt * v[i]
        else:
            x[i] = x[i-1] + dt * v[i-1]
            v[i] = x[i-1] + dt * a[i-1]

    return t, x, v, a

def launch_vector(mag, incline, azimuth=False, radians=False):
    ''' Return v0 vector for given scalar magnitude and incline above the horizon. 

        Args:
            magnitude (float):      magnitude of v0 (m/s)
            incline (float):        angle above horizon (degrees)
            azimuth (float):        angle in plane of horizon (degrees)
            radians (bool):         option for using radian incline

        Returns:
            np.array (np.float64):  vector with launch velocity components
    '''
    
    if not radians:
        incline = incline * (180.0 / np.pi)
        
        if azimuth:
            azimuth = azimuth * (180.0 / np.pi)
    
    if azimuth:
        z = mag * np.sin(incline)
        h = mag * np.cos(incline)

        x = h * np.cos(azimuth)
        y = h * np.sin(azimuth)

        return np.asarray([x, y, z])

    else:
        x = mag * np.cos(incline)
        y = mag * np.sin(incline)

        return np.asarray([x, y])

