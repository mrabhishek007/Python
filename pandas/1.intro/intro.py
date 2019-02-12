import pandas as pd

df = pd.read_csv('./weather.csv')

max_temperature = df["Temperature"].max()
print(f'Max Temperature is {max_temperature}')

get_raining_date = df['EST'][df['Events'] == 'Rain']  # cond : find 'EST' if 'EVENTS' = 'Rain'
print(f'List of date on which it rain : \n {get_raining_date}')


# replacing 'invalid' value with 0
df.fillna(0, inplace=True)
avg_wind_speed = df['WindSpeedMPH'].mean() # finding avg
print(f'Avg wind speed : {avg_wind_speed}')



print(df)

