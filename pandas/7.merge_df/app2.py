# Merging Based  on common column (Not bases on index)

import pandas as pd

df1 = pd.DataFrame({
    "city": ["new york", "chicago", "orlando", "punjab"],
    "temperature": [21, 14, 35, 18],
})

df2 = pd.DataFrame({
    "city": ["chicago", "new york", "orlando", "berlin"],
    "humidity": [65, 68, 75, 36],
})

# similar to joins of sql

# This will only show intersection of both df, similar to Inner Join , so we can use other method to show all data
# here city is common in both df, so we can merge w.r.t city name even the city order is in different format, very powerful
df3 = pd.merge(df1, df2, on="city")
print(df3)

# (Show Union of data) similar to Outer Join
df3 = pd.merge(df1, df2, on="city", how="outer")
print(df3)

# (Show complete data of 1st df) similar to Left Join
df3 = pd.merge(df1, df2, on="city", how="left")
print(df3)

# (Show complete data of 2nd df) similar to Right Join
df3 = pd.merge(df1, df2, on="city", how="right")
print(df3)

# show complete data with indicator( shows which data is coming from which df)
df3 = pd.merge(df1, df2, on="city", how="outer", indicator=True)
print(df3)

# ********************DEALING WITH DATA WITH MORE THAN ONE SAME COLUMN**********************************

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})

df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})

# by default if the 2 column has same name it will show x and y as their name. we can rather give our own suffix name to those columns
df3= pd.merge(df1,df2,on="city",how="outer", suffixes=('_first','_second'))
print(df3)











