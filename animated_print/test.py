from animated_plot import animated_plot
from animated_plot import animated_scatter
import numpy as np

x = np.linspace(-1*np.pi, 1*np.pi, 4*100)
y = np.c_[np.sin(x), np.cos(x)]
x = np.c_[x, x]

#animated_plot(x,y, label=['sin','cos'], marker=[None, '+'], ls=['-', ':'], update_len=0.00001)
animated_scatter(x,y, label=['sin','cos'], marker=[None, '+'], update_len=0.00001)