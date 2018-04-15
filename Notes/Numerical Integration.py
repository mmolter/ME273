import numpy as np
import matplotlib.pyplot as plt

def function(x):
    ''' An arbitary function we want to integrate. '''

    return 0.085*x**3 - 1.5*x**2 + 12*x - 13


def integrate(func, a, b, dx=0.1, method='left'):
    ''' A remann integrating function 
    
        Args:

            func (function):    Arbitrary function to integrate
            a (float):          starting point
            b (float):          stopinng point
            dx (float):         dx for integration

            method (string):    'left'      -- left-hand remann
                                'right'     -- right-hand remann
                                'mid'       -- middle point remann
                                'trapezoid' -- trapezoidal sum
    
    '''

    assert method in ['left', 'right', 'mid', 'trapezoid']

    x = np.arange(a, b, dx)
    y = func(x)

    if method = 'left':
        integral = sum(y * dx)
        

print(integrate(function, 0, 10, 0.11, method='rigxt'))
