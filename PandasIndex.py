import pandas as pd
import numpy as np

#series
fruits = {'oringe': 2, 'banana': 3, 'apple': 4, 'peach': 5}
series = pd.Series(fruits)
#print(series)
#print(series[0:-1], '\n', series[['peach']])
#print(series.index)
#print(series.values)
series = series.append(pd.Series([3], index=['grape']))
#print(series)
series = series.drop('banana')
#print(series)
conditions = [True,True,False,False]
#print(series[conditions])
#print(series[series >= 4])
#print(series.sort_index)
#print(series.sort_values(ascending=False))

#dataflame
data = {'fruits': ['apple', 'oringe', 'banana', 'strawberry', 'kiwifruit'],
'year': [2000, 2001, 2002, 2003, 2019],
'time': [1,4,6,8,3]}
df1 = pd.DataFrame(data)
#print(df1)

index = ['apple', 'oringe', 'banana', 'strawberry', 'kiwifruit']
data1 = [10,5,8,2,7]
data2 = [39,13,52,24,14]
series1 = pd.Series(data1, index=index)
series2 = pd.Series(data2, index=index)
df = pd.DataFrame([series1,series2])
#print(df)
df.index = [1,2]
#print(df)

series = pd.Series(['mango', 2008, 9], index=['fruits', 'year', 'time'])
df = df1.append(series, ignore_index=True)
#print(df)
df['price'] = [150, 130, 100, 300, 200, 400]
#print(df)

#参照 loc[インデックスのリスト、カラムのリスト]
dfloc = df.loc[[1,2],['time','year']]
#print(dfloc)
#np.random.seed(0)
#df = pd.DataFrame()
#for i in index:
#    df[i] = np.random.choice(range(1,11), 10)
#df.index = range(1,11)
#print(df)
#df = df.loc[range(2,6),['banana', 'kiwifruit']]
#print(df)

# iloc[行番号のリスト、列番号のリスト]
dfiloc = df.iloc[[1,3],[0,2]]
#print(dfloc)
#np.random.seed(0)
#df = pd.DataFrame()
#for i in index:
#    df[i] = np.random.choice(range(1,11), 10)
#df.index = range(1,11)
#print(df)
#df = df.iloc[range(1,5),[2, 4]]
#print(df)

# 行列の削除 列を削除する場合はaxis=1を与える
df1 = df.drop(range(0,2))
#print(df1)
df2 = df.drop('year', axis=1)
#print(df2)

# sort カラムもしくはカラムのリスト、ascending=True,False
df = df.sort_values(by='year', ascending=True)
#print(df)

# フィルタリング
#print(df.index % 2 == 0)
#print(df[df.index % 2 == 0])

np.random.seed(0)
df = pd.DataFrame()
for i in index:
    df[i] = np.random.choice(range(1,11), 10)
df.index = range(1,11)
print(df)
df = df.loc[df['apple'] >= 5]
df = df.loc[df['kiwifruit'] >= 5]
print(df)