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
print(f'Valor médio dos encargos totais: R${media}')