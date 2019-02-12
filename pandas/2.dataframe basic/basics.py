import pandas as pd
df = pd.read_csv('./data.csv')

print(df)

# print few rows of  dataframe
print(df.head())



# print exactly 3 rows of  dataframe
print(df.head(3))



# print last rows of  dataframe
print(df.tail(2))


# print  rows  between 2 - 5 of  dataframe
print(df[2:5])


# print  only even rows from beginning
print(df[::2])


# print columns of df
print(df.columns)


# Access specific col columns of df in following ways (same) :
# print(df.day)
# print(df['day'])
# print(df.get('day'))

# print multiple columns
print(df[ ['event', 'day'] ])

# conditionally selecting df
print(df[df.temperature >= 31])

# printing the row where temp is max
print( df[df.temperature == df['temperature'].max()] ) #recommended
print( df[df.temperature == df.temperature.max()] ) # valid


# printing only specific col when temp is max
print(df[['day', 'temperature']] [df.temperature == df['temperature'].max()])

# set index (inpace allows to replace the current dt, by default new data-table will be created)
df.set_index('day', inplace=True)

# finding data based on index
print(df.loc['1/5/2017'])

# reset ur index to original one
print(df.reset_index(inplace=True))

print(df)











