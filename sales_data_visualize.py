# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 00:19:45 2020

@author: aravind.ramdas
"""
import matplotlib.pyplot as plt

def plot_month_sales(best_sales_month):
    #Plotting the sales by month chart
    months = range(1,13)
    plt.bar(months, best_sales_month['Sales'])
    plt.xticks(months)
    plt.ylabel('Sales in USD ($)')
    plt.xlabel('Month Number')
    plt.show()

def plot_city_sales(best_sales_city, csv_data):    
    #Plotting the sales by city chart
    cities = [city for city, df in csv_data.groupby('City')]
    plt.bar(cities, best_sales_city['Sales'])
    plt.xticks(cities, rotation='vertical', size=8)
    plt.ylabel('Sales in USD ($)')
    plt.xlabel('City name')
    plt.show()

def plot_most_sold_products(csv_data,quantity_ordered, product_group):
    products = [product for product, csv_data in product_group]
    plt.bar(products, quantity_ordered)
    plt.ylabel('Quantity Ordered')
    plt.xlabel('Product')
    plt.xticks(products, rotation='vertical', size=8)
    plt.show()

def plot_most_sold_products_prices(csv_data,quantity_ordered, product_group, prices):
    products = [product for product, csv_data in product_group]
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.bar(products, quantity_ordered, color='g')
    ax2.plot(products, prices, 'b-')    
    ax1.set_xlabel('Product Name')
    ax1.set_ylabel('Quantity Ordered', color='g')
    ax2.set_ylabel('Price ($)', color='b')
    ax1.set_xticklabels(products, rotation='vertical', size=8)    
    plt.show()