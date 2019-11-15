# AnimatedPlot Document:

## Author Info: 
* Name: Kent010341 (Nickname using on internet)
* e-mail: kent010341@gmail.com

---
## Class Info:
AnimatedPlot is made for easily used to plot several lines or dots based on well-known matplotlib.

---
## Parameters:
* No parameter.

---
## Methods:
* plot(self, \*xy_data, fixed=False, color=None, c=None, marker=None, linestyle=None, ls=None, linewidth=None, lw=None, label=None):
  * Most of the parameters are same as [matplotlib.pyplot.plot](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html).
  * If the parameter **fixed** is True, line will be fully shown instead of animated updating.
* scatter(self, x_data, y_data, fixed=False, color=None, c=None, marker=None, label=None):
  * Most of the parameters are same as [matplotlib.pyplot.scatter](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html).
  * If the parameter **fixed** is True, scatter will be fully shown instead of animated updating.
* show(self, update_len=0.001, fixed_frame=True, frame_expand=0.2):
  * update_len: Time paused between every frame updating. Unit: second.
  * fixed_frame: Use maximum and minimum value of x_data and y_data as frame size.
  * frame_expand: Expand the fixed frame by this rate. Currently doesn't work on 0.