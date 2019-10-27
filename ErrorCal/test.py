import numpy as np
from ErrorCal import cal_mse, cal_mae, cal_rmse, cal_mape, ErrorCal

x = np.linspace(0, 4*np.pi, 4000)
sin = np.sin(x)
noisy_sin = x + np.random.uniform(-1e-3, 1e-3, sin.shape[0])

print('cal_mse:', cal_mse(sin, noisy_sin))
print('cal_mae:', cal_mae(sin, noisy_sin))
print('cal_mape:', cal_mape(sin, noisy_sin))
print('cal_rmse:', cal_rmse(sin, noisy_sin))

error = ErrorCal(sin, noisy_sin)
print('MSE:', error.MSE)
print('MAE:', error.MAE)
print('MAPE:', error.MAPE)
print('RMSE:', error.RMSE)