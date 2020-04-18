# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:03:08 2020

@author: aravind.ramdas
"""
#Library intialization
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter
import sales_data_cleaner as data_cleaner
import sales_data_visualize as data_visualize

#read master csv file
sales_master_data = pd.read_csv('sales_master_data.csv')
#clean rows with empty/NaN values
sales_master_data = data_cleaner.remove_nan_rows(sales_master_data)

#Sales analysis based on city
sales_master_data = data_cleaner.create_month_column(sales_master_data)
sales_master_data['Sales'] = sales_master_data['Quantity Ordered'] * sales_master_data['Price Each']
best_sales_month =  sales_master_data.groupby('Month').sum()
data_visualize.plot_month_sales(best_sales_month)

#Sales analysis based on city
sales_master_data = data_cleaner.create_city_column(sales_master_data)
best_sales_city = sales_master_data.groupby('City').sum()
data_visualize.plot_city_sales(best_sales_city, sales_master_data)

#Advertisement display timing to maximize likelihood of customer's buying product
#sales_master_data['Order Date'] = pd.to_datetime(sales_master_data['Order Date'])
#print(sales_master_data.head())
#include new column Hour and Minute
#sales_master_data['Hour'] = sales_master_data['Order Date'].dt.hour
#sales_master_data['Minute'] = sales_master_data['Order Date'].dt.minute
#print(sales_master_data.head())
#plotting the results in line chart
#hours = [hour for hour, df in sales_master_data.groupby('Hour')]
#plt.plot(hours, sales_master_data.groupby(['Hour']).count())
#plt.xticks(hours)
#plt.grid()
#plt.show()

#Products most often sold together
#prod = sales_master_data[sales_master_data['Order ID'].duplicated(keep=False)]
#prod['Grouped'] = prod.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
#prod = prod[['Order ID', 'Grouped']].drop_duplicates()
#print(prod.head(20))
#count = Counter()

#for row in prod['Grouped']:
#    row_list = row.split(',')
#    count.update(Counter(combinations(row_list, 2)))

#for key, value in count.most_common(10):
#    print(key, value)

#Products sold most and why its sold most
product_group = sales_master_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']
data_visualize.plot_most_sold_products(sales_master_data, quantity_ordered, product_group)

#Products sold most and its prices
prices = sales_master_data.groupby('Product').mean()['Price Each']
data_visualize.plot_most_sold_products_prices(sales_master_data, quantity_ordered, product_group, prices)
