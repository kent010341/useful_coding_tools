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
* title(self, str_title):
  * Set the title.
* xlabel(self, str_xlabel):
  * Set the label of x axis.
* ylabel(self, str_ylabel):
  * Set the label of y axis.
* show(self, update_len=0.001, fixed_frame=True, frame_expand=0.2):
  * Showing the lines and scatters animatedly.
    * update_len: Time paused between every frame updating. Unit: second.
    * fixed_frame: Use maximum and minimum value of x_data and y_data as frame size.
    * frame_expand: Expand the fixed frame by this rate. Currently doesn't work on 0.
* save_gif(self, save_dir='./', use_time_as_name=True, file_name=None, interval=100, repeat_delay=1000):
  * Save the animated plot as gif.
    * save_dir: The folder that used to save the gif file.
    * use_time_as_name: Using current time as file name.
    * file_name: If use_time_as_name is False, file_name is needed to be set.
    * interval: gif update interval. Change this to make it faster or slower.
    * repeat_delay: gif update repeat delay.
