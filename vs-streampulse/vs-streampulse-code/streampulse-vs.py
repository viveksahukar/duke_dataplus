#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:08:04 2019

@author: vs
"""
# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read file and convert dateTime column into datetime format
df = pd.read_csv('flagged_sites.csv', sep=',', encoding='latin_1', infer_datetime_format=True)
df.dateTimeUTC = pd.to_datetime(df.dateTimeUTC)


df1 = df.copy() # making a copy of the original dataframe
df1 = df.drop(columns=['flagID', 'flagComment']) # dropping comments column for range checking
sites = df1.siteID.unique() # creating array of all site names


#save each siteID in separate wide dataframe with each variable as column
sites_df = dict()
for site in sites:
    data = df1.loc[df1['siteID']==site]
    data1 = data.pivot_table(index='dateTimeUTC', columns='variable', values='value')
    norm_data1 = (data1 - data1.mean())/data1.std()
    sites_df.update({site:norm_data1})


sites_list = []
for key in sites_df.keys():
    sites_list.append(key)

# plot boxplot for each variable for every siteID
plt.figure(figsize=(30, 20))

for i in range(28):
    plt.subplot(4, 7, i+1)
    sites_df[sites_list[i]].boxplot(vert=0)
    plt.title(sites_list[i])

plt.tight_layout()
plt.show()

# creating boxplots for each variable by siteID

df2 = df.copy() # making a second copy of the original dataframe
df2 = df.drop(columns=['flagID', 'flagComment']) # dropping comments column for range checking
variables = df2.variable.unique() # creating array of all variable names

#save each variable in separate wide dataframe with each variable as column
variables_df = dict()
for variable in variables:
    data2 = df2.loc[df2['variable']==variable]
    data3 = data2.pivot_table(index='dateTimeUTC', columns='siteID', values='value')
    norm_data2 = (data3 - data3.mean())/data3.std()
    variables_df.update({variable:norm_data2})

variables_list = []
for key in variables_df.keys():
    variables_list.append(key)
    
# plot boxplot for each variable for every siteID
plt.figure(figsize=(30, 20))

for i in range(28):
    plt.subplot(4, 7, i+1)
    variables_df[variables_list[i]].boxplot(vert=0)
    plt.title(variables_list[i])
    
plt.tight_layout()
plt.show()


