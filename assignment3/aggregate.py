import pandas as pd

df = pd.read_csv("/Users/ryansponzilli/Developer/UIUC/is477/is477-fa24-ryants4/assignment3/input/Food_Inspections_50k.csv")
df = df.groupby("Facility Type", dropna=False).agg('count').reset_index()
df = df.rename(columns={"Facility Type": "Facility_Type", "Inspection ID": "Count"})
df = df[["Facility_Type", "Count"]]
df = df.sort_values(["Count","Facility_Type"], ascending=True)

df.to_csv("results/pandas-fac-types.csv", index=False)