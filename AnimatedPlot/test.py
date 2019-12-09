import matplotlib.pyplot as plt
import numpy as np

from AnimatedPlot import AnimatedPlot

ap = AnimatedPlot()

x = np.linspace(-5, 5, 100)
y = x ** 2
ap.plot(x, y, label='x^2')
ap.scatter(x, x**3, label='x^3')
ap.plot([-5, 5], [0, 0], fixed=True)
ap.title('test')
ap.xlabel('x label')
ap.ylabel('y label')
ap.show()
ap.save_gif()
