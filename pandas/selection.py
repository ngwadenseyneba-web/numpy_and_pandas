import pandas as pd

#df = pd.read_csv("data.csv")

df = pd.read_csv("data.csv", index_col= "Name")
'''
#print(df["Name"].to_string())
#print(df["Height"].to_string())
#print(df["Weight"].to_string())
#print(df["Legendary"].to_string())
#print(df["Type1"].to_string())
#print(df[["Name", "Weight"]].to_string())

# Selection by row
#print(df.loc["Ivysaur": "Blastoise", ["Height", "Weight"]])

print(df.iloc[:50:-1, 0:3].to_string())'''

pokemon = input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")