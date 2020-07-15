#  exponential weighted moving average
import pandas as pd

airline = pd.read_csv('./airline_passengers.csv', index_col='Month', parse_dates=True)
airline.dropna(inplace=True)

#print(airline.head())
airline['6-month-SMA'] = airline['Thousands of Passengers'].rolling(window=6).mean()
airline['12-month-SMA'] = airline['Thousands of Passengers'].rolling(window=12).mean()
airline['EWMA-12'] = airline['Thousands of Passengers'].ewm(span=12).mean()
airline[['Thousands of Passengers','EWMA-12']].plot(figsize=(12,8))
