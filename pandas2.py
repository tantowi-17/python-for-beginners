import pandas as pd

# Read the csv file
pda = pd.read_csv("sales.csv", header=0)
df = pd.DataFrame(pda)
df['Date'] = pd.to_datetime(df['Date'])

# How much is the total sales revenue of the data
total_revenue = df['Total'].sum()
print('How much is the total sales revenue of the data       : ', total_revenue)

# total quantity of all the sold items
total_quantity = df['Quantity'].sum()
print('How many are the total quantity of all the sold items : ', total_quantity)

# total quantity of all the sold items
unit_price = df['Unit price'].max()
print('What is the most expensive item that is sold          : ', unit_price)

# Gender does generate more sales
gender = df['Gender'].max()
print('Which Gender does generate more sales                 : ', gender)

# total sales revenue in February 2019
month_2 = df[df['Date'].apply(lambda x:x.month == 2)]
total_month_2 = month_2['Total'].sum()
print('How much is the total sales revenue in February 2019  : ', total_month_2)

# popular Product Line in January 2019
month_1 = df[df['Date'].apply(lambda x:x.month == 1)]
total_most = month_1.groupby(['Product line'])
data_total = total_most['Quantity'].sum()
print('What is the most popular Product Line in January 2019 : ', data_total)