import pandas as pd

# skips 1st row from beginning and create df
df = pd.read_csv('./stock_data.csv', skiprows=1)
print(df)

# removes the header and setting custom header
df = pd.read_csv('./stock_data.csv', skiprows=1, header=None, names=['A', 'B', 'C', 'D', 'E'])
print(df)

# only loading some specific number of rows from csv
df = pd.read_csv('./stock_data.csv', nrows=3)
print(df)

# replace the specific values eg: [ n.a., not available ] values to 'NaN' wherever it is present in the csv file
df = pd.read_csv('./stock_data.csv', na_values=['n.a.', 'not available'])
print(df)

# replace the specific values only on specific rows to 'NaN', in above example all values which is 'na' or 'not available' is converted to 'NaN'
# but if we wan't to convert only specific value in a col to 'NaN'  we use dicionary instead of list

df = pd.read_csv("stock_data.csv", na_values={
    'eps': ['not available'],
    'revenue': [-1],
# only revenue col val is replaced with 'NaN' where -1 is found bcz revenue cannot be negative, it won't effect other columns with -1 values
    'people': ['not available', 'n.a.']
})
print(df)

#  ********************************   WRITING TO CSV        ************************************************

# write csv without header and index
df.to_csv('output.csv', index=False, header=False)

#  only export 2 columns from dataframe

df.to_csv('output1.csv', index=False, columns=['tickers', 'eps'])


# converter to convert messy data into meaning-full data

def convert_people_cell(people):
    if (people == 'n.a.'):
        return 'Vikash Kumar Guarav'
    else:
        return people


def convert_price_cell(price):
    if (price == 'n.a.'):
        return 0
    else:
        return price




df = pd.read_csv('./stock_data.csv', converters={
    'people': convert_people_cell,  # converting people col  data to a meaningful data if 'n.a.' is found
    'price': convert_price_cell # converting price col  data to 0  if 'n.a.' is found
})

print(df)
df.to_excel('newexcel.xlsx', sheet_name='stocks' , index=False)


# writing a excel file with multiple sheets
weather_df = pd.read_csv('./weather.csv')
with pd.ExcelWriter('stocks_weather.xlsx') as Writer:
    df.to_excel(Writer, sheet_name='stocks')
    weather_df.to_excel(Writer, sheet_name='weather')

print('DONE')

