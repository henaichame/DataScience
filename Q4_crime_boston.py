import pandas as pd
import re
from pandas.api.types import CategoricalDtype

filename = "./file/Airbnb_NYC_2019.csv"
df = pd.read_csv(filename, low_memory=False)
# crime = pd.read_csv(filename, low_memory=False)
# print(crime)

num_rows = df.shape[0]
num_cols = df.shape[1]
print(df.head())
print("before drop column=", df.shape[1])
df.drop(columns=['SHOOTING'], inplace=True)
print("after drop column=", df.shape[1])
print(df.head())

# Missing value cleaning
df['Lat'] = df['Lat'].fillna(0)
df['Long'] = df['Long'].fillna(0)
print(df.head())

# Correlation verification
df['Lat'] = df.Lat.astype(float)
df['Long'] = df.Long.astype(float)
print("start Correlation verification")
for i in range(num_rows):
    if (abs(df.Lat[i] - float(re.split(',', df.Location[i])[0][1:])) > 1e-3):
        print("Lat ", i, ",", df.Lat[i], ",", float(re.split(',', df.Location[i])[0][1:]))
    if (abs(df.Long[i] - float(re.split(',', df.Location[i])[1][1:-1])) > 1e-3):
        print("Long ", i, ",", df.Long[i], ",", float(re.split(',', df.Location[i])[1][1:-1]))
print("end Correlation verification")

# Extracting information from Complex values

df['OCCURRED_ON_DATE'] = pd.to_datetime(df['OCCURRED_ON_DATE'])


def create_features(df):
    df['dayofweek'] = df['OCCURRED_ON_DATE'].dt.dayofweek
    df['quarter'] = df['OCCURRED_ON_DATE'].dt.quarter
    df['dayofyear'] = df['OCCURRED_ON_DATE'].dt.dayofyear
    df['dayofmonth'] = df['OCCURRED_ON_DATE'].dt.day
    df['weekofyear'] = df['OCCURRED_ON_DATE'].dt.weekofyear

    X = df[['dayofweek', 'quarter', 'dayofyear', 'dayofmonth', 'weekofyear']]
    return X


create_features(df).head()

df.quarter = df.quarter.astype(CategoricalDtype())
df.dayofweek = df.dayofweek.astype(CategoricalDtype())
df.dayofyear = df.dayofyear.astype(CategoricalDtype())
df.dayofmonth = df.dayofmonth.astype(CategoricalDtype())
print(df.head())
