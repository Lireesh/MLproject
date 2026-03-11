import seaborn as sns
df = sns.load_dataset("tips")
import numpy as np
df.isnull().sum()
df['sex']=df['sex'].map({'Female':0,'Male':1}).astype(int)
df['smoker']=df['smoker'].map({'No':0,'Yes':1}).astype(int)
df['time']=df['time'].map({'Lunch':0,'Dinner':1}).astype(int)
df['day']=df['day'].map({'Thur':0,'Fri':1,'Sat':2,'Sun':3}).astype(int)
print(df.head())
print(df.info())