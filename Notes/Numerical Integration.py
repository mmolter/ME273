import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 15
dt = 0.01

x = np.arange(a, b, dt) 
y = np.sin(x)
Y = np.empty_like(x)

dt = x[1] - x[0]
for i in range(x.size):
	Y[i] = Y[i-1] + y[i-1] * dt

plt.plot(x, y)
plt.plot(x, Y)
plt.plot(x, 1 - np.cos(x))
plt.show()

print(x)
print(y)
print(Y)
