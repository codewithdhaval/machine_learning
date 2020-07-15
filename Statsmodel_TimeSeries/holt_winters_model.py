import pandas as pd
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing

airline = pd.read_csv('./airline_passengers.csv', index_col='Month', parse_dates=True)
airline = airline.dropna()
airline.index.freq = 'MS'
span = 12
alpha = 2/(span + 1)
airline['EWMA-12'] = airline['Thousands of Passengers'].ewm(alpha=alpha, adjust=False).mean()

model = SimpleExpSmoothing(airline['Thousands of Passengers'])
fitted_model = model.fit(smoothing_level=alpha, optimized=False)

airline['DES_add_12'] = ExponentialSmoothing(airline['Thousands of Passengers'], trend='add').fit().fittedvalues.shift(-1)

airline['DES_mul_12'] = ExponentialSmoothing(airline['Thousands of Passengers'], trend='mul').fit().fittedvalues.shift(-1)
airline[['Thousands of Passengers', 'DES_add_12', 'DES_mul_12']].plot(figsize=(12, 8))

airline['TES_mul_12'] = ExponentialSmoothing(airline['Thousands of Passengers'], trend='mul', seasonal='mul', seasonal_periods=12).fit().fittedvalues

#airline[['Thousands of Passengers', 'DES_mul_12', 'TES_mul_12']].plot(figsize=(12, 8))
