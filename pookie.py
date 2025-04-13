import pandas as pd

df=pd.read_csv('newFile.csv')

# print(df)



# print(df.iloc[0])
# print(df.loc[0][1])
# print(df.at[0,'Name'])

df['salary']=[100,100]

print(df)

print('_____________-')

df.drop('salary',axis=1,inplace=True)

df['Age']=df['Age']+10
print(df)