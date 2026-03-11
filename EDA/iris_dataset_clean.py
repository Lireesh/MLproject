import seaborn as sns
df=sns.load_dataset('iris')
print(df.head())

print(df['species'].unique())
df['species']=df['species'].map({'setosa':1, 'versicolor':2, 'virginica':3})
print(df.head())
print(df.info())


'''
penguins
titanic
flights
fmri
diamonds
mpg
planets
car_crashes
anscombe
dots
exercise
geyser

'''
