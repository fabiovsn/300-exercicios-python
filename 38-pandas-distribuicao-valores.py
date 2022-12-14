import pandas as pd
import numpy as np

url = ("https://ml-repository-krakers.s3-eu-west-1.amazonaws.com/kaggle+/churn_modelling/Telco-Customer-Churn.csv")

df = pd.read_csv(url)

print(df.columns)

df.drop('OnlineBackup', inplace=True, axis=1)
df.drop('OnlineSecurity', inplace=True, axis=1)
df.drop('TechSupport', inplace=True, axis=1)
df.drop('MultipleLines', inplace=True, axis=1)
df.drop('DeviceProtection', inplace=True, axis=1)
df.drop('PaperlessBilling', inplace=True, axis=1)
df.drop('PaymentMethod', inplace=True, axis=1)

media = df['TotalCharges'][df['TotalCharges']!=' '].median()
df.loc[df['TotalCharges'] == ' ', 'TotalCharges'] = media
df['TotalCharges'] = df['TotalCharges'].astype('float')

categorica = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
              'PhoneService', 'InternetService', 'StreamingTV',
              'Contract', 'StreamingMovies', 'Churn']

numerica = ['tenure', 'MonthlyCharges']

for col in categorica:
    df[col] = pd.Categorical(df[col])

for col in numerica:
    df[col] = df[col].astype(float)

# print(df.info())
#
# print(df.describe(include=['category']))
print(df['Churn'].value_counts())