import pandas as pd

# making day col. as python date format, default format is string
df = pd.read_csv('weather-data.csv', parse_dates=['day'])
df.set_index('day', inplace=True)
print(df)

# filling missing data 'NaN' with specific value on columns
new_df = df.fillna({
    # 'temperature': df['temperature'].mean(), # filling missing val with avg temp
    "windspeed": 0,
    "event": 'No event'
})
print(new_df)

# filling missing val with its last valid col valu ex :  d[5][3] = 30 then d[5][4] will also be 40 if it is NaN
new_df_forward = new_df.fillna(method='ffill')  # forward fill
# new_df = new_df.fillna(method='bfill') # backward fill
print(new_df_forward)

# filling missing val with its last valid col and next valid col avg eg: d[5][3] = 30 , d[5][5] = 50, d[5][3] = (30+ 50)/2 if d[5][4] is NaN
new_df_interpolate = new_df.interpolate()
print(new_df_interpolate)

# when method = time is used, unlike above statement it just doesn't find the avg it find the estimated val w.r.t date of index
new_df_interpolate = new_df.interpolate(method='time')
print(new_df_interpolate)


# Drop the rows where at least one element is missing.
complete_row_df = df.dropna()
print(complete_row_df)

# Drop the rows where all elements are missing.
complete_row_df = df.dropna(how="all")
print(complete_row_df)

# Drop the rows where atleast 2 valid value is available
complete_row_df = df.dropna(thresh=2)
print(complete_row_df)


# crating additional missing index between 01-01-2017 to 01-01-2017
dt = pd.date_range("01-01-2017", "01-11-2017")
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)
print(df)
