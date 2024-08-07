#converting to dataframe
import pandas as pd
data = [
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]
df=pd.DataFrame(data,columns=['Name','Age','City'])
print(df)
#slicing rows
b1=df.iloc[0:2]
print(b1)
#slicing columns
b2=df.iloc[:,:2]
print(b2)
#get particular elements
b3=df.iloc[2,2]
print(b3)
#Based on specific conditions
fil_b=df[df['Age']>30]
print(fil_b)
#set particular column as index
s=df.set_index('City')
print(s)
#To get rows based on specific values
b_3=s.loc['Los Angeles':]
print(b_3)
#Dealing with missing values
#Find
a = [
    ['Alice', 30,None],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', None, 'Chicago']
]
b=pd.DataFrame(a,columns=['Name','Age','City'])
print(pd.isnull(b))
print(pd.isna(b))
print(pd.notna(b))
print(pd.notnull(b))
