import pandas as pd
from statsmodels.tsa.filters.hp_filter import hpfilter

df = pd.read_csv('./macrodata.csv')
## what does hpfilter do ?
gdp_cycle, gdp_trend = hpfilter(df['realgdp'],lamb=1600)
#gdp_trend.plot()
df['trend'] = gdp_trend
df[['trend','realgdp']][190:].plot(figsize=(12,5))