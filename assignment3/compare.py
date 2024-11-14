import pandas as pd

df_pandas = pd.read_csv("results/pandas-fac-types.csv")
df_sql = pd.read_csv("results/sql-fac-types.csv")

compare = df_pandas.compare(df_sql)
compare.to_csv("results/comparison.csv", index=True)