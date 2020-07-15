#ETS - Error Trend Seassonality
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

airline = pd.read_csv('./airline_passengers.csv', index_col='Month', parse_dates=True)
airline = airline.dropna()
result = seasonal_decompose(airline['Thousands of Passengers'], model='multiplicative')
result.plot()
