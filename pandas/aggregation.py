import pandas as pd

# Aggregate fubctions = Reduces a set of values into a single value
#                       Used to summerize and analyze data
#                       Often used with the groupby() method

df = pd.read_csv("data.csv")

#print(df.mean(numeric_only=True))
#print(df.sum(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.count())

# single column
#print(df["Height"].mean())
#print(df["Weight"].sum())
#print(df["Legendary"].min())
#print(df["Weight"].max())
#print(df["Type2"].count())

group = df.groupby("Type1")

#print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].max())
