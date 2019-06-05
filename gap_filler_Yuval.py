import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as pltdates
import datetime as dt
import scipy as sy
import scipy.fftpack as syfp
import pylab as pyl

from main_functions import readFile, getData, plotGraph

myfile = readFile()

#given a data form, and a start and end, which are dates in the same format as in the main .csv file
def gapFill(DataForm, start_date, end_date):
    duration = dt.timedelta(end_date) - dt.timedelta(start_date)
    start_hour = start_date.hours
    start_minute = start_date.minutes
    i = 0
    while(DataForm['dateTimeUTC'].iloc[i].hours != start_hour & DataForm['dateTimeUTC'].iloc[i].minutes != start_minute):
        i++
    square_difs = dict()
    while(DataForm['dateTimeUTC'].iloc[i] < DataForm['dateTimeUTC'].iloc[-1] - duration):       #index -1 means the last index in the dataform
        if(DataForm['dateTimeUTC'].iloc[i] == start_date):
            while(DataForm['dateTimeUTC'].iloc[i] <= end_date):
                i++
        else:
            dictindex = DataForm['dateTimeUTC'].iloc[i]
            while(DataForm['dateTimeUTC'].iloc[i] < dictindex + duration):
                currentdate = DataForm['dateTimeUTC'].iloc[i]
                while(DataForm['dateTimeUTC'].iloc[i] == currentdate):
                    key = [DataForm['dateTimeUTC'].iloc[i], DataForm['variable'].iloc[i]]

            sum = 0
            for j in xrange(96):

            i += 96
