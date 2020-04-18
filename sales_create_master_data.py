# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:36:02 2020

@author: aravind.ramdas
"""

import pandas as pd
import os

#Fetch file list from directory
files = [file for file in os.listdir('./Sales_Data')]

#create empty dataframe to save all file data
sales_master_data = pd.DataFrame()

#Iterate through the file list and concat into single file
for file in files:
    df = pd.read_csv('./Sales_Data/'+file)
    sales_master_data = pd.concat([sales_master_data, df])

sales_master_data.to_csv("sales_master_data.csv", index=False)