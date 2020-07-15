import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

airline = pd.read_csv('./airline_passengers.csv', index_col='Month', parse_dates=True)
airline.index.freq= 'MS'
train_data = airline.iloc[:109]
test_data = airline.iloc[108:]
fitted_model = ExponentialSmoothing(train_data['Thousands of Passengers'],trend='mul', seasonal='mul', seasonal_periods=12).fit()
test_predictions = fitted_model.forecast(36)

train_data['Thousands of Passengers'].plot(legend=True, label='Train', figsize=(12,8))
test_data['Thousands of Passengers'].plot(legend=True, label='Test')
test_predictions.plot(legend=True, label='Prediction')
