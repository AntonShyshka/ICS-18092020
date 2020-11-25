import matplotlib.pyplot as plt
from numpy import cos, arange
t = arange(0, 10.0, 0.01)
x = arange(0, 10.0, 0.01)
plt.plot(t, -x**cos(5*x))
plt.show() 