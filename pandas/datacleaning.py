import pandas as pd

#data cleaning : the process of fixing/removing:
#                incomplete, incorrect, or irrelevant data
#                ~75% of work donw with pandas is data cleaning
 

df = pd.read_csv("data.csv")

# drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])

# handle missing data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2" : "None"})

# Fix inconsistent values
'''df["Type1"] = df["Type1"].replace({"Grass" : "GRASS", 
                                   "Fire" : "FIRE",
                                   "Water" : "WATER"})
                                   '''

#Standardize text
#df["Name"] = df["Name"].str.lower()

# Fix Data types
# df["Legendary"] = df["Legendary"].astype(bool)

# Remove duplicate values
df = df.drop_duplicates()

print(df.to_string())

