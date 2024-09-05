import datetime as dt
import pandas as pd

df = pd.read_csv('lab2/private_data.csv', sep='|')
df.to_csv('lab2/deidentified_data.csv')

# Suppress `name` and `phone`
df.drop(columns=['name', 'phone'], inplace=True)

# Generalize the Address
df['zip'] = df['address'].str[-5:]
df.drop(columns=['address'],inplace=True)
df.head()

# Perturb the Birthdate
study_date = dt.datetime(2024, 1, 1)
df['birthdate'] = pd.to_datetime(df['birthdate'])
df['age'] = study_date - df['birthdate']
df.drop(columns=['birthdate'])
df.head()