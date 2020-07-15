import pandas as pd

df = pd.read_csv('starbucks.csv', index_col='Date', parse_dates=True)
df['Close'].plot(xlim=['2017-01-01','2017-03-01'], ylim=[50,60])

