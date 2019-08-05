# DetailRecorder Document:

## Author Info: 
* Name: Kent010341 (Nickname using on internet)
* e-mail: kent010341@gmail.com

---
## Class Info:
DetailRecorder is made for easily recording that may be able to prevant from some accidents like unpredictable computer shutting down, or recording all detail of algorithms that is generally needed lots of time.

---
## Parameters:
* detail_dir: str
  * The direction of a folder that the document of detail is saved. If detail_dir doesn't exisit, all of the inexistent folder will automatically be created.

* use_time_as_name: bool (default=True)
  * Use current time as file name.
* file_name: str (default=None)
  * Needed if use_time_as_name is False, and it won't be used while use_time_as_name is True.
* encoding: str (default='utf-8-sig')
  * Type of encoding used to write the document.
* show_time: bool (default=False)
  * Add full text of time in front of the input text.

---
## Methods:
* dprint(self, \*strings, enable_var_former=True):
  * **Avaiable for any type!!**
  * Multiple parameters or even no parameter given is avaiable. enable_var_former is defaultly set as True, which will change *list*, *tuple*, *numpy.ndarray*, *dict* into a form that can directly used as a variable for further coding.
