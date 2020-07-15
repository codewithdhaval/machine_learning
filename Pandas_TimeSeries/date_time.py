import matplotlib
import pandas as pd
import numpy as np

matplotlib
data = np.random.randn(3,2)
cols = ['A','B']
print(data)

idx = pd.date_range('7/8/2018', periods=3, freq='D')
df = pd.DataFrame(data, index=idx, columns=cols)
print(df.index)