import pandas as pd
import string

calories = {"Day 1" : 1750, "Day 2" : 2100, "Day 3" : 1700}

series = pd.Series(calories)

print(series)

'''
data = [100, 102, 104, 200, 202]

series = pd.Series(data, index = list(string.ascii_lowercase[:5]))

#print(series.loc["a"])

print(series[series < 200])
'''

'''
series.loc["c"] = 200

print(series)

print(series.iloc[2])
'''