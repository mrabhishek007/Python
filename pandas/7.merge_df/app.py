import pandas as pd

india_weather = pd.DataFrame({
    "city": ["mumbai", "delhi", "banglore"],
    "temperature": [32, 45, 30],
    "humidity": [80, 60, 78]
})

print(india_weather)

us_weather = pd.DataFrame({
    "city": ["new york", "chicago", "orlando"],
    "temperature": [21, 14, 35],
    "humidity": [68, 65, 75]
})
print(us_weather)

# simply append the row with new data with separate index
df = pd.concat([india_weather, us_weather])
print(df)

# simply append the row with new data but has common index
df = pd.concat([india_weather, us_weather], ignore_index=True)
print(df)

# shows the DataFrame with separate keys
df = pd.concat([india_weather, us_weather], keys=["india", "us"])
print(df)
print(df.loc["us"])  # accessing above df with key
print(df.loc["india"])


# Merging two DataFrame on columns and matching the index, so that the data will be in correct city

temperature_df = pd.DataFrame({
    "city": ["mumbai", "delhi", "banglore"],
    "temperature": [32, 45, 30],
}, index=[0, 1, 2])
windspeed_df = pd.DataFrame({
    "city": ["delhi", "mumbai"],
    "windspeed": [7, 12],
}, index=[1, 0])
df = pd.concat([temperature_df,windspeed_df],axis=1) # axis will help to append col instead of append row
print(df.fillna(0))


# Appending an existing DataFrame with series with column
s = pd.Series(["Humid","Dry","Rain"], name="event")
df = pd.concat([temperature_df, s], axis=1) # we can pass multiple data frame also
print(df)






