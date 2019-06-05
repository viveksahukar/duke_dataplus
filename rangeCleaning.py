import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as pltdates
import datetime as dt


test_data = pd.read_csv('flagged_sites.csv')
ranges = pd.DataFrame({'DO_mgL': [0, 25],
                        'WaterTemp_C': [-5, 50],
                        'pH': [2, 11],
                        'AirTemp_C': [-100, 60],
                        'WaterPres_kPa': [0, 0]})



def getData(DataForm, region, site, variable):
    regionFile = DataForm.loc[DataForm['regionID']==region]
    siteFile = regionFile.loc[regionFile['siteID']==site]
    return siteFile.loc[siteFile['variable']==variable]      #return dirty file (all flags are kept) for given region, site, and variable name

def plotGraph(DataForm):
    #import these libraries in the following way, in order for this to work:
    #import matplotlib.pyplot as plt
    #import matplotlib.dates as pltdates
    #import datetime as dt
    #use on data extracted using 'getData' helper function
    dates = [dt.datetime.strptime(d,'%m/%d/%y %H:%M').date() for d in DataForm.dateTimeUTC]
    datenums = pltdates.date2num(dates)
    fig1, ax1 = plt.subplots();
    ax1.plot_date(dates, DataForm.value)
    region = DataForm.loc[:, 'regionID']
    site = DataForm.loc[:,'siteID']
    variable = DataForm.loc[:,'variable']
    ax1.set_title(region.iloc[0] + ', ' + site.iloc[0] + ', ' + variable.iloc[0])
    return

def basicRangeCleaner(DataForm):
    #takes a cleaned up data set of a single variable, takes out obvious outliers detected using a flat range.
    #uses global variable 'ranges', containing ranges for each variable
    variables = DataForm.loc[:,'variable']
    range = ranges.loc[:,variables.iloc[0]]
    return DataForm.loc[(DataForm['value']>range[0]) & (DataForm['value']<range[1])]

def stndRangeCleaner(DataForm):
    #takes a data set of a single variable, takes out values lying outside a range of 4 standard deviations
    values = DataForm.loc[:, 'value']
    val_mean = values.mean()
    range_std = [val_mean - DataForm.std()*4 , val_mean + DataForm.std()*4]
    return DataForm.loc[(DataForm['value']>range_std[0]) & (DataForm['value']<range_std[1])]

def stndMonthRangeCleaner(DataForm):
    #takes a data set of a single variable, takes out values lying outside a range of 2 standard deviations for each month
    DataForm['month'] = pd.DatetimeIndex(DataForm['dateTimeUTC']).month
    monthly_clean = DataForm.set_index(['regionID', 'siteID', 'dateTimeUTC', 'variable',
        'flagID', 'flagComment', 'month']).groupby('month').apply(filter_vals)\
        .reset_index().dropna()
    monthly_clean = monthly_clean.drop(['month'], axis=1)
    monthly_clean =  monthly_clean.reindex(columns = ['regionID', 'siteID', 'dateTimeUTC', 'variable', 'value',
       'flagID', 'flagComment'])
    return monthly_clean

def filter_vals(x):
    std_val = x.std()
    mean_val = x.mean()
    filtered = x[(x < mean_val + std_val*2) & (x>mean_val - std_val*2)]
    return filtered

#def stndMonthRangeCleaner(DataForm):
    #takes a data set of a single variable, goes through month-by-month and removes values outside a range of 4 std per month
#    rangeMonthClean = pd.DataFrame()     #creates empty DataFrame containing cleaned data
#    for j in range(1,13):
#        for i in DataForm.itertuples():     #loops through FataFrame input
#            monthly = pd.DataFrame()
#            if((dt.datetime.strptime(i[3], '%m/%d/%y %H:%M').date()).month == j):
#                monthly.append(pd.Series(i), ignore_index=True)       #append to monthly data
#            rangeMonthClean.append(stndRangeCleaner(monthly))       #appends cleaned monthly data to large cleaned data variable
#    return rangeMonthClean




DataForm = getData(test_data, 'NC', 'UEno', 'WaterTemp_C')
DataForm.head()
DataForm.shape
DataForm['value'].max()
DataForm['value'].min()
plotGraph(DataForm)
DataForm = stndMonthRangeCleaner(DataForm)
DataForm.head()
DataForm.shape
DataForm['value'].max()
DataForm['value'].min()
plotGraph(DataForm)




az_DOmgL = getData(test_data, 'AZ', 'LV', "DO_mgL")
values = az_DOmgL.loc[:, 'value']
val_mean = values.mean()
range_std = [val_mean - az_DOmgL.std()*4 , val_mean + az_DOmgL.std()*4]
print(range_std[0])
print(az_DOmgL['value'])

#az_DOmgL_rangeClean = stndRangeCleaner(az_DOmgL)
#az_DOmgL_rangeClean.tail(10)

#az_DOmgL_rangeMonthClean = pd.DataFrame() # creates empty dataframe
#for i in az_DOmgL.itertuples():
#    #print(pd.Series(i))
#    for j in range (1,13):
#        monthly = pd.DataFrame()
#        if (dt.datetime.strptime(i[3], '%m/%d/%y %H:%M').date()).month == j:
#            #print((dt.datetime.strptime(i[3], '%m/%d/%y %H:%M').date()).month)
#            monthly.append(pd.Series(i), ignore_index=True)
#        if not monthly.empty:
#            az_DOmgL_rangeMonthClean.append(monthly)
