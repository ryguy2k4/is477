import datetime as dt
import pandas as pd
import numpy as np

df = pd.read_csv('lab2/private_data.csv', sep='|')
df.to_csv('lab2/deidentified_data.csv')

# Suppress `name` and `phone`
df.drop(columns=['name', 'phone'], inplace=True)

# Generalize the Address
df['zip'] = df['address'].str[-5:]
df.drop(columns=['address'],inplace=True)

# Perturb the Birthdate
study_date = dt.datetime(2024, 1, 1)
df['birthdate'] = pd.to_datetime(df['birthdate'])
df['age'] = (study_date - df['birthdate'])/dt.timedelta(365)
df.drop(columns=['birthdate'],inplace=True)
df.head()
np.random.seed(123)
random_years = np.random.randint(low=1,high=4,size=df.shape[0])
df['age'] = round(df['age'] + random_years)
df.head()

# Pseudonymization
import hmac
import hashlib

with open("lab2/secret.txt") as f:
    secret_key = f.readline().strip()

df['id'] = df['ssn'].apply(
    lambda x:
       hmac.new(
        bytes(secret_key, 'latin-1'),
        msg=bytes(x, 'latin-1'),
        digestmod=hashlib.sha256
        ).hexdigest() 
)
df.drop(columns=['ssn'],inplace=True)

# Export Anonymized Data
df.to_csv("lab2/deidentified_data.csv")