import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as pltdates
import datetime as dt

myfile = pd.read_csv("flagged_sites.csv", sep=',', parse_dates=True)

def getData(DataForm, region, site, variable):
    #import numpy as np
    #import pandas as pd
    regionFile = DataForm.loc[DataForm['regionID']==region]
    siteFile = regionFile.loc[regionFile['siteID']==site]
    return siteFile.loc[siteFile['variable']==variable]      #return dirty file (all flags are kept) for given region, site, and variable name

def plotGraph(DataForm):
    #import these libraries in the following way, in order for this to work:
    #import matplotlib.pyplot as plt
    #import matplotlib.dates as pltdates
    #import datetime as dt
    #use on data extracted using 'getData' helper function
    dates = [dt.datetime.strptime(d,'%Y-%m-%d %H:%M:%S').date() for d in DataForm.dateTimeUTC]
    datenums = pltdates.date2num(dates)
    plt.plot_date(dates, DataForm.value)
    region = DataForm.loc[:, 'regionID']
    site = DataForm.loc[:,'siteID']
    variable = DataForm.loc[:,'variable']
    plt.title(region.iloc[0] + ', ' + site.iloc[0] + ', ' + variable.iloc[0])
    return

#unique vars:
#['Battery_V' 'CDOM_ppb' 'DO_mgL' 'DOsat_pct' 'Depth_m' 'SpecCond_uScm'
# 'Turbidity_NTU' 'WaterTemp_C' 'pH' 'pH_mV' 'AirTemp_C' 'Light2_lux'
# 'Light3_lux' 'Light5_lux' 'Light_lux' 'WaterPres_kPa' 'CDOM_mV'
# 'SpecCond_mScm' 'Turbidity_mV' 'AirPres_kPa' 'CO2_ppm' 'Light_PAR'
# 'Nitrate_mgL' 'Light4_lux' 'Discharge_m3s' 'Level_m' 'satDO_mgL'
# 'WaterTemp2_C']

NC_Eno_WaterTempC = getData(myfile, 'NC', 'Eno', 'WaterTemp_C')
plotGraph(NC_Eno_WaterTempC)

ranges = pd.DataFrame({'DO_mgL': [0, 25],
                        'WaterTemp_C': [-5, 50],
                        'pH': [2, 11],
                        'AirTemp_C': [-100, 60],
                        'WaterPres_kPa': [0, 0]})

def basicRangeCleaner(DataForm):
    #takes a cleaned up data set of a single variable, takes out obvious outliers detected using a flat range.
    #uses global variable 'ranges', containing ranges for each variable
    variables = DataForm.loc[:,'variable']
    range = ranges.loc[:,variables.iloc[0]]
    return DataForm.loc[(DataForm['value']>range[0]) & (DataForm['value']<range[1])]

NC_Eno_WaterTempC_basicClean = basicRangeCleaner(NC_Eno_WaterTempC)
plotGraph(NC_Eno_WaterTempC_basicClean)
