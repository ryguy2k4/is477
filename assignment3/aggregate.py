import pandas as pd

df = pd.read_csv("input/Food_Inspections_50k.csv")
df = pd.DataFrame(df.value_counts("Facility Type")).reset_index()
df = df.rename(columns={"Facility Type": "Facility_Type", "count": "Count"})
df = df.sort_values(["Count", "Facility_Type"], ascending=True)
df.to_csv("results/pandas-fac-types.csv", index=False)