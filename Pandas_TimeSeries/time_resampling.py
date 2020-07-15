import pandas as pd

df = pd.read_csv('starbucks.csv', index_col='Date', parse_dates=True)
#df['Close'].resample('A').mean().plot.bar(title='Yearly Mean Closing Price for Starbucks')


## resample by year
df['Close'].resample('A').mean().plot.bar()
## resampel by month
df['Close'].resample('M').mean().plot.bar()
#title = "Monthly Max closing price for Starbucks"
#df['Close'].resample('M').max().plot.bar(title=title)