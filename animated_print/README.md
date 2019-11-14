# animated_plot Document:

## Author Info: 
* Name: Kent010341 (Nickname using on internet)
* e-mail: kent010341@gmail.com

---
## Methods Info:
This file animated_plot is made for easily used to plot several lines or dots based on well-known matplotlib. 

---
## Methods:
### animated_plot(<params>):
#### Parameters:
* \*xy_data: array
  * Can input one or two parameters, where one means y_data, and two means x_data and y_data. x is optional, defaultly use range(len(y)) as x.
  * If multiply line needed to be shown, make x_data and y_data into 2-D array. Check test.py get detailed example.
* color: str, list or tuple (default=None)
  * Line color, support list of different color.
  * Check [this](https://matplotlib.org/3.1.1/tutorials/colors/colors.html) for more information.
* c: str, list or tuple (default=None)
  * Same as the parameter **color**.
* marker: str, list or tuple (default=None)
  * Line marker, support list of different marker.
  * Check [this](https://matplotlib.org/3.1.1/api/markers_api.html) for more information.
* linestyle: str, list or tuple (default=None)
  * Line style, support list of different line style.
  * Check [this](https://matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html) for more information.
* ls: str, list or tuple (default=None)
  * Same as the parameter **linestyle**.
* linewidth: int, list or tuple (default=None)
  * Line width, support list of different line width.
* lw: int, list or tuple (default=None)
  * Same as the parameter **linewidth**. 
* label: str, list or tuple (default=None)
  * Line label, support list of different line label.
* update_len: float (default=0.001)
  * Time paused between every frame updating. Unit: second.
* fixed_frame: bool (default=True)
  * Use maximum and minimum value of x_data and y_data as frame size.
* frame_expand: float (default=0.2)
  * Expand the fixed frame by this rate.

### animated_scatter(<params>):
#### Parameters:
* \*xy_data: array
  * Can input one or two parameters, where one means y_data, and two means x_data and y_data. x is optional, defaultly use range(len(y)) as x.
  * If multiply line needed to be shown, make x_data and y_data into 2-D array. Check test.py get detailed example.
* color: str, list or tuple (default=None)
  * Line color, support list of different color.
  * Check [this](https://matplotlib.org/3.1.1/tutorials/colors/colors.html) for more information.
* c: str, list or tuple (default=None)
  * Same as the parameter **color**.
* marker: str, list or tuple (default=None)
  * Line marker, support list of different marker.
  * Check [this](https://matplotlib.org/3.1.1/api/markers_api.html) for more information.
* label: str, list or tuple (default=None)
  * Line label, support list of different line label.
* update_len: float (default=0.001)
  * Time paused between every frame updating. Unit: second.
* fixed_frame: bool (default=True)
  * Use maximum and minimum value of x_data and y_data as frame size.
* frame_expand: float (default=0.2)
  * Expand the fixed frame by this rate.