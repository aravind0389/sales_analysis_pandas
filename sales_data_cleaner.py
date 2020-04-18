# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 01:16:16 2020

@author: aravind.ramdas

Functions to clean unwanted data and include new columns for data analytics
"""
import pandas as pd

def remove_nan_rows(csv_data):
    #Find NaN in the csv data    
    csv_data = csv_data.dropna(how='all')    
    return csv_data

def create_month_column(csv_data):
    #include new column month
    csv_data['Month'] = csv_data['Order Date'].str[0:2]
    #clear unwanted column header values appended during file creation
    csv_data = csv_data[csv_data['Order Date'].str[0:2] != 'Or']
    csv_data['Quantity Ordered'] = pd.to_numeric(csv_data['Quantity Ordered'])
    csv_data['Price Each'] = pd.to_numeric(csv_data['Price Each'])
    csv_data['Month'] = csv_data['Month'].astype('int32')
    return csv_data

def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]

def create_city_column(csv_data):
    csv_data['City'] = csv_data['Purchase Address'].apply(lambda x: get_city(x)+' ('+get_state(x)+')')
    return csv_data