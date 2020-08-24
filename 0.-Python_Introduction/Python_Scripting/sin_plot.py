import matplotlib.pyplot as plt
import numpy as np

""" numpy.arange([start, ]stop, [step, ]dtype=None)
Return evenly spaced values within a given interval. """

x = np.arange(0,4*np.pi,0.01)
y = np.sin(x)

plt.plot(x,y)
plt.show()
