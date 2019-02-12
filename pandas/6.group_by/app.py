# In this tutorial we are going to look at weather data from various cities and see how group by can be used to run some analytics.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("weather_by_cities.csv")
print(df)

# For this dataset, get following answers,
# 1. What was the maximum temperature in each of these 3 cities?
# 2. What was the average windspeed in each of these 3 cities?

group = df.groupby("city")  # returns pandas group obj

# by iterating group we get new data frame for each cities

for city, df in group:
    print("city:", city)
    print("\n")
    print("data:", df)

# This is similar to SQL,
# SELECT * from weather_data GROUP BY city


mumbai_df = group.get_group('mumbai')
print(mumbai_df)

print(group.max())  # returns max temp of all the cities
print(group.mean())  # returns avg temp of all the cities
print(group.min())  # returns min temp of all the cities

print(group.describe())  # describes temp of all the cities

print(group.size())  # tells total size of rows in each group

print(group.count())  # total count of columns each cities

group.plot()
plt.show()
