import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())
#print(df['col2'].unique())
#print(df['col1'] > 2)
newdf = df[(df['col1']>0) & (df['col2'] == 444)]
print("========================")
print(newdf)

def times2(x):
    return x*2

print("========================")
print(df['col1'].apply(times2))

print("========================")
print(df.sort_values(by='col2'))
print("========================")
print(df)