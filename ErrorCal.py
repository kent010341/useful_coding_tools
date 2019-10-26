import numpy as np
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import mean_absolute_error as MAE

def _flatten(arr_1, arr_2, check_same_len=True):
	flat_arr_1 = np.array(arr_1).reshape(-1)
	flat_arr_2 = np.array(arr_2).reshape(-1)

	if check_same_len:
		assert flat_arr_1.shape[0] == flat_arr_2.shape[0], 'Both of the arrays should have same size.'

	return flat_arr_1, flat_arr_2

def cal_mse(real, predict):
	arr_real, arr_predict = _flatten(real, predict)

	return MSE(arr_real, arr_predict)

def cal_mae(real, predict):
	arr_real, arr_predict = _flatten(real, predict)

	return MAE(arr_real, arr_predict)

def cal_rmse(real, predict):
	return cal_mse(real, predict) ** 0.5

def cal_mape(real, predict):
	arr_real, arr_predict = _flatten(real, predict)

	return np.mean(np.abs((arr_real - arr_predict) / arr_predict)) *100