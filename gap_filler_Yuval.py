import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as pltdates
import datetime as dt
import scipy as sy
import scipy.fftpack as syfp
import pylab as pyl

from main_functions import readFile, getData, plotGraph

myfile = readFile();

NC_Eno_WaterTempC = getData(myfile, 'NC', 'Eno', 'WaterTemp_C')
plotGraph(NC_Eno_WaterTempC)

#given a data form, and a start and end, which are dates in the same format as in the main .csv file
def gapFill(DataForm, start, end):
    start_date = dt.datetime.strptime(start,'%Y-%m-%d %H:%M:%S').date()
    end_date = dt.datetime.strptime(end,'%Y-%m-%d %H:%M:%S').date()
    duration = dt.timedelta(end_date) - dt.timedelta(start_date)
    duration /= dt.timedelta(minutes=15)
    start_hour = start_date.hours
    start_minute = start_date.minutes
    startindex = 0
    for i in xrange(96):        #how many 15 minute intervals exist in one day
        thisdate = dt.datetime.strptime(DataForm.iloc[i,0],'%Y-%m-%d %H:%M:%S').date()
        if(thisdate.hours = start_hour & thisdate.minutes = start_minute):
            startindex = i
            break
        #need to fix this loop (and all loops) because DataForm will have multiple entries for one date!
    i = 0
    square_difs = np.array((len(DataForm)-startindex)/96, 1)
    skipindex = ( dt.timedelta(start_date) - dt.timedelta(dt.datetime.strptime(DataForm.iloc[startindex,0],'%Y-%m-%d %H:%M:%S').date()) ) / dt.timedelta(minutes = 15)
    while i < len(square_difs):
        if(i = skipindex):
            i += 96
            continue
        sum = 0
        for j in xrange(96):

        i += 96
