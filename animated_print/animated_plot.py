import matplotlib.pyplot as plt
import numpy as np

def animated_plot(
	*xy_data, 
	color=None, c=None, 
	marker=None,
	linestyle=None, ls=None,
	linewidth=None, lw=None,
	label=None,
	update_len=0.001,
	fixed_frame=True,
	frame_expand=0.2):
	
	if len(xy_data) == 2:
		x_data, y_data = xy_data
	elif len(xy_data) == 1:
		y_data = xy_data[0]
		x_data = list(range(len(y_data)))
	else:
		raise ValueError('Too many parameters given.')
	
	x_data = np.array(x_data)
	y_data = np.array(y_data)
	if len(x_data.shape) == 1:
		x_data = x_data.reshape(-1, 1)
		y_data = y_data.reshape(-1, 1)

	_check_input(x_data, y_data, c, color, marker, label, update_len, linestyle, ls,linewidth, lw)

	# Get fixed frame size
	if fixed_frame:
		max_x, min_x, max_y, min_y = _get_frame_size(x_data, y_data, frame_expand)

	for i in range(data_len):
		plt.clf()
		if fixed_frame:
			plt.xlim(min_x, max_x)
			plt.ylim(min_y, max_y)
		for j, [c, marker, ls, lw, label] in enumerate(zip(seq_c, seq_marker, seq_ls, seq_lw, seq_label)):
			plt.plot(x_data[:i+1, j], y_data[:i+1, j], c=c, marker=marker, ls=ls, lw=lw, label=label)
		plt.grid()
		plt.legend()
		plt.pause(update_len)

def animated_scatter(
	x_data, y_data, 
	color=None, c=None, 
	marker=None,
	label=None,
	update_len=0.001,
	fixed_frame=True,
	frame_expand=0.2):
	_check_input(x_data, y_data, c, color, marker, label, update_len)
	# Get fixed frame size
	if fixed_frame:
		max_x, min_x, max_y, min_y = _get_frame_size(x_data, y_data, frame_expand)
	for i in range(data_len):
		plt.clf()
		if fixed_frame:
			plt.xlim(min_x, max_x)
			plt.ylim(min_y, max_y)
		for j, [c, marker, label] in enumerate(zip(seq_c, seq_marker, seq_label)):
			plt.scatter(x_data[:i+1, j], y_data[:i+1, j], c=c, marker=marker, label=label)
		plt.grid()
		plt.legend()
		plt.pause(update_len)

def _check_input(x_data, y_data, c, color, marker, label, update_len, linestyle=None, ls=None, linewidth=None, lw=None):
	global seq_c, seq_marker, seq_ls, seq_lw, seq_label

	# Check x, y.
	_xy_checker(x_data, y_data)
	# Check color
	seq_c = _arr_params_checker(c, color, type_cons=str)
	# Check marker
	seq_marker = _arr_params_checker(marker, type_cons=str)
	# Check linestyle
	seq_ls = _arr_params_checker(linestyle, ls, type_cons=str)
	# Check linewidth
	seq_lw = _arr_params_checker(linewidth, lw, type_cons=int)
	# Check label
	seq_label = _arr_params_checker(label, type_cons=str)
	# Check update_len
	assert np.ceil(float(update_len)) > 0, 'update_len must be a number greater than 0.'

def _xy_checker(x_data, y_data):
	global line_num, data_len, dim

	assert np.all(x_data.shape == y_data.shape), 'x_data and y_data must have same size.'
	dim = len(x_data.shape)
	assert dim <= 2, 'x_data and y_data must be 1-D or 2-D.'
	if dim == 1:
		line_num = 1
	else:
		line_num = x_data.shape[-1]
	data_len = x_data.shape[0]

def _arr_params_checker(*params, type_cons):
	for param in params:
		seq = list()
		if isinstance(param, type(None)):
			temp_seq = [None]
		elif isinstance(param, type_cons):
			temp_seq = [param]
		elif type(param) in [list, tuple]:
			temp_seq = list(param)

		for i in range(line_num):
			try:
				seq.append(temp_seq[i])
			except:
				seq.append(None)

	return seq

def _get_frame_size(x_data, y_data, frame_expand):
	max_x, min_x = np.max(x_data), np.min(x_data)
	max_x = np.abs(np.sign(max_x) + np.sign(max_x) * frame_expand) * max_x
	min_x = np.abs(np.sign(min_x) + np.sign(min_x) * frame_expand) * min_x
	max_y, min_y = np.max(y_data), np.min(y_data)
	max_y = np.abs(np.sign(max_y) + np.sign(max_y) * frame_expand) * max_y
	min_y = np.abs(np.sign(min_y) + np.sign(min_y) * frame_expand) * min_y

	return max_x, min_x, max_y, min_y