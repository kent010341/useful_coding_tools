import numpy as np
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import mean_absolute_error as MAE

# Call Function. ==========================================================================================
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

def cal_mape(real, predict, minima=1e-6):
    arr_real, arr_predict = _flatten(real, predict)

    # Deal with divided by 0
    denominators = arr_real.copy()
    condition = denominators == 0
    denominators[condition] += minima

    return np.mean(np.abs((arr_real - arr_predict) / denominators)) *100

# Call Class. ==========================================================================================
class ErrorCal():
    def __init__(self):
        pass

    def insert_data(self, real, predict, minima=1e-6):
        self._minima = minima
        self._arr_real, self._arr_predict = self._flatten(real, predict)
        self._error_index()

    def _flatten(self, arr_1, arr_2):
        flat_arr_1 = np.array(arr_1).reshape(-1)
        flat_arr_2 = np.array(arr_2).reshape(-1)

        assert flat_arr_1.shape[0] == flat_arr_2.shape[0], 'Both of the arrays should have same size.'
        self._N = flat_arr_1.shape[0]

        return flat_arr_1, flat_arr_2

    def _error_index(self):
        error_arr = np.abs(self._arr_real - self._arr_predict)

        mae_val = 0
        mse_val = 0
        mape_val = 0

        for i in range(self._N):
            mae_val += error_arr[i]
            mse_val += error_arr[i] ** 2
            if self._arr_real[i] != 0:
                mape_val += error_arr[i] / self._arr_real[i]
            else:
                mape_val += error_arr[i] / self._minima
        # MAE
        self.MAE = mae_val / self._N
        # MSE
        self.MSE = mse_val / self._N
        # MAPE
        self.MAPE = mape_val / self._N * 100
        # RMSE
        self.RMSE = np.sqrt(self.MSE)
