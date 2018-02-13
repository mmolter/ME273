import numpy as np
import pytest

from implementation import (acceleration, velocity_exact, position_exact, 
	euler_projectile, exact_projectile, absolute_error, relative_error)


def test_acceleration():
	D = 0.5
	rho = 1.29
	mass = 0.625
	g = 9.8

	radius = 0.12
	area = radius * np.pi**2

	assert acceleration(vel=-1.174, D=D, rho=rho, mass=mass, g=g, area=area) == pytest.approx(9.767, 0.01)

