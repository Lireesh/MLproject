'''
import kagglehub

# Download latest version
path = kagglehub.dataset_download("jillanisofttech/flight-price-prediction-dataset")

print("Path to dataset files:", path)

'''


import pandas as pd
import seaborn as sns
print("hi")
flight_data=pd.read_excel(r"C:\Users\VLireesh\Desktop\MLprojects\EDA\flight_dataset\Data_Train.xlsx")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)
#print(flight_data.info())
#column additional info clean

flight_data['Additional_Info']=flight_data['Additional_Info'].map({'In-flight meal not included':1,'No check-in baggage included':2,'No info':0})
#print(flight_data['Additional_Info'].value_counts())
#print(flight_data['Additional_Info'].unique())

#flight_data['Date_of_Journey']=pd.to_datetime(flight_data['Date_of_Journey'],infer_datetime_format=True)
flight_data['date']=flight_data['Date_of_Journey'].str.split('/').str[0]
flight_data['month']=flight_data['Date_of_Journey'].str.split('/').str[1]
flight_data['year']=flight_data['Date_of_Journey'].str.split('/').str[2]
flight_data.drop('Date_of_Journey',axis=1,inplace=True)

flight_data['Dept_hour']=flight_data['Dep_Time'].str.split(':').str[0]
flight_data['Dept_min']=flight_data['Dep_Time'].str.split(':').str[1]
flight_data.drop('Dep_Time',axis=1,inplace=True)

flight_data['Dept_hour']=flight_data['Dept_hour'].astype(int)
flight_data['Dept_min']=flight_data['Dept_min'].astype(int)


flight_data['Arrival_Time']=flight_data['Arrival_Time'].str.split('').str[0]


flight_data['Arrival_hour']=flight_data['Arrival_Time'].str.split(':').str[0]
flight_data['Arrival_min']=flight_data['Arrival_Time'].str.split(':').str[1]
flight_data.drop('Arrival_Time',axis=1,inplace=True)

#flight_data['Arrival_hour']=flight_data['Arrival_hour'].astype(int)
#light_data['Arrival_min']=flight_data['Arrival_min'].astype(int)

flight_data['Total_Stops']=flight_data['Total_Stops'].map({'non-stop':0, '1 stop':1, '2 stops':2,'3 stops':3, '4 stops':4, 'nan':1  })

flight_data.drop(6474,axis=0,inplace=True)
flight_data['Dur_hour']=flight_data['Duration'].str.split(' ')
flight_data['Dur_min']=flight_data['Duration'].str.split(' ')

print(flight_data.head())
