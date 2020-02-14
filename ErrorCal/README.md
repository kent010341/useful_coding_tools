# ErrorCal Document:

## Author Info: 
* Name: Kent010341 (Nickname using on internet)
* e-mail: kent010341@gmail.com

---
## Tool Info:
* ErrorCal is made for calculating regression loss such as mean absolute error(MAE), mean square error(MSE), etc.
* **Class** type and **Method** type supported.
* Automatically reshape to 1-D array.
---

## Class type:
> Calculating all kind of loss.
### Parameters:
* real: array-like
  * Array of real values.
* predict: array-like
  * Array of predictive values.

### Methods:
* insert_data(self, real, predict, minima=1e-6):
  * Insert real and predict data.
  * Parameter "minima" is set to prevent from divided by zero while calculating MAPE.

### Attributes:
* MAE: float
  * Mean absolute error.
* MSE: float
  * Mean square error.
* MAPE: float
  * Mean absolute percentage error.
* RMSE: float
  * Root mean square error.
---

## Method Type:
### Methods:
* cal_mae(real, predict):
  * Return mean absolute error
* cal_mse(real, predict):
  * Return mean square error.
* cal_mape(real, predict, minima=1e-6):
  * Return mean absolute percentage error.
  * Parameter "minima" is set to prevent from divided by zero while calculating MAPE.
* cal_rmse(real, predict):
  * Return root mean square error.
