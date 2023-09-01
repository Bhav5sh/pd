import pandas as pd
import numpy as np
df1=pd.read_csv(r"C:\Users\user\Downloads\archive\IPL Player Stats\Batting Stats\BATTING STATS - IPL_2017.csv")
df2=pd.read_csv(r"C:\Users\user\Downloads\archive\IPL Player Stats\Bowling Stats\BOWLING STATS - IPL_2017.csv")
print(df1.head())
print(df2.head())
print(np.ndim(df1))
print(np.ndim(df2))
print(df1.describe())
print(df1.info())
print(df2.info())
print(df1.isnull().sum())
print(df2.isnull().sum())
df1['Player']=df1['Player'].convert_dtypes()
# print(df1['Player'])
print(df1.info())
df2['Player']=df2['Player'].convert_dtypes()
df2['BBI']=df2['BBI'].convert_dtypes()

print(df2.info())
print(df1['Player'][df1['Runs'].idxmax()])
print(df2['Player'][df2['Wkts'].idxmax()])
fig={'batesman':['David warner','Gautam gambhir','Shikhar dhawan','Suresh raina','Hashim amla'],
'bowler':['Bhuvneshwar kumar','jaydev unadkat','jasprit bumraha','imran tahir','Rashid khan'],
'wicket-keepers':['kuldeep yadav','Axar patel','Ben stokes','Rishabh pant','sanju samson'],
'All-ronuder':['steve smith','robin uthappa','kieron pollard','sunil narine','Yuvaraj singh']}
optimal_number=pd.DataFrame(fig)
print(optimal_number.T)
a=df1['Player'].head(7).tolist()
print(a)
b=df2['Player'].head(7).tolist()
print(b)
print(df1.head(7))
print(df2.head(7))
l=[a[:],b[:4]]
print(l)
print(r"C:\Users\user\Documents\Cricketing Insights.pdf")
