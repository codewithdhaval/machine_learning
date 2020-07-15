from sklearn.metrics import mean_squared_error, mean_absolute_error
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def findError() -> None:
    print("find error")
    airline = pd.read_csv('./airline_passengers.csv', index_col='Month', parse_dates=True)
    airline.index.freq = 'MS'
    train_data = airline.iloc[:109]
    test_data = airline.iloc[108:]
    fitted_model = ExponentialSmoothing(train_data['Thousands of Passengers'], trend='mul', seasonal='mul',
                                        seasonal_periods=12).fit()
    test_predictions = fitted_model.forecast(36)
    print(f'Mean Squared Error - {mean_squared_error(test_data, test_predictions)}') #5614.30554
    print(f'Mean Absolute Error - {mean_absolute_error(test_data, test_predictions)}') #63.0309


if __name__ == "__main__":
    findError()