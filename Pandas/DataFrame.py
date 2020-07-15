import pandas as pd
import numpy as np

labels = ['a','b','c']
mylist = [10,20,30]
arr = np.array(mylist)

print(f'Pandas Series : {pd.Series(data=mylist,index=labels)}')

df = pd.DataFrame({'A':[1,2, np.nan],'B':[5, np.nan,6],'C':[1,2,3]})
print(f'Dataframe :\n {df}')

print(f'Drop nan :\n {df.dropna()}')

print(f'Fill nan :\n {df.fillna(value=0)}')

df_groupby = df.groupby('A').sum()
print(f'GroupBy A :\n {df_groupby}')
