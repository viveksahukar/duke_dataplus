import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as pltdates
import datetime as dt
from main_functions import readFile, getData, plotGraph

def daily_average(DataForm):
    #takes in a DataFrame containing all information for one siteID, returns DataFrame containing daily averages of each variable
    DataForm['month'] = pd.DatetimeIndex(DataForm['dateTimeUTC']).month
    DataForm['day'] = pd.DatetimeIndex(DataForm['dateTimeUTC']).day
    variables = az_lv.variable.unique()
    byVar = pd.DataFrame()
    for v in variables:
        values = DataForm.loc[DataForm['variable']==v]
        #values = values.groupby(['month','day']).mean()
        values = values.set_index(['regionID', 'siteID', 'dateTimeUTC', 'variable', 'flagID', 'flagComment', 'day', 'month']).groupby(['month', 'day']).apply(filter_vals)
        byVar = byVar.append(values)
    return byVar

def filter_vals(x):
    mean_val = x.mean()
    filtered = mean_val
    return filtered



myfile = readFile();
az_lv = getDataSite(myfile, 'AZ', 'LV')
daily = daily_average(az_lv)

daily.head()

def getDataSite(DataForm, region, site):
    #import numpy as np
    #import pandas as pd
    regionFile = DataForm.loc[DataForm['regionID']==region]
    return regionFile.loc[regionFile['siteID']==site]      #return dirty file (all flags are kept) for given region, site, and variable name






az_lv['month'] = pd.DatetimeIndex(az_lv['dateTimeUTC']).month
az_lv['day'] = pd.DatetimeIndex(az_lv['dateTimeUTC']).day

variables = az_lv.variable.unique()

az_byVar = pd.DataFrame()

for v in variables:
    values = az_lv.loc[az_lv['variable']==v]
    #values = values.groupby(['month','day']).mean()
    values = values.set_index(['regionID', 'siteID', 'dateTimeUTC', 'variable', 'flagID', 'flagComment', 'day', 'month']).groupby(['month', 'day']).apply(filter_vals)
    az_byVar = az_byVar.append(values)

az_byVar.head()
