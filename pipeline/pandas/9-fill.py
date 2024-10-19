#!/usr/bin/env python3
from_file = __import__('2-from_file').from_file
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# YOUR CODE HERE
df.drop(columns=['Weighted_Price'])
df['Close'] = df['Close'].ffill()

for column in ['High', 'Low', 'Open']:
    df[column] = df[column].fillna(df['Close'])

df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

print(df.head())
print(df.tail())