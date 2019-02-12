import pandas as pd
import numpy as np
df = pd.read_csv("weather_list.csv")


# Replacing single value

new_df = df.replace(-99999, value=np.NaN)
print(new_df)

# Replacing list of single value
new_df = df.replace(to_replace=[-99999,-88888], value=0)
print(new_df)

# Replacing per column
new_df = df.replace({
        'temperature': -99999,
        'windspeed': -99999,
        'event': '0'
    }, np.nan)
print(new_df)


# Replacing by using mapping
new_df = df.replace({
        -99999: np.nan,
        'no event': 'Sunny',
    })
print(new_df)

# when windspeed is 6 mph, 7 mph etc. & temperature is 32 F, 28 F etc.
new_df = df.replace({'temperature': '[A-Za-z]', 'windspeed': '[a-z]'},'', regex=True)
print(new_df)


# Replacing list with another list
df = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})
print(df)
df = df.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4])
print(df)



