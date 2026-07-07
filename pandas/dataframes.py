import pandas as pd

data = {"Name": ["Rick", "Morty", "Summer", "Beth", "Jerry"],
        "Age": [70, 14, 17, 34, 45]}

df = pd.DataFrame(data)

#add a new column to the dataframe

df["Job"] = ["Scientist", "Adventurer", "Student", "Doctor", "Unemployed"]

#add a new row to the dataframe
new_row = pd.DataFrame([{"Name": "Alice", "Age": 25, "Job": "Engineer"}, {"Name": "Bob", "Age": 30, "Job": "Designer"},])

df = pd.concat([df, new_row], ignore_index=True)

print(df)