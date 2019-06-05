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
    while(DateForm.iloc[i,2].hours != start_hour & DateForm.iloc[i,2].minutes != start_minute):        #how many 15 minute intervals exist in one day
        i++
    square_difs = dict()
    while(DataForm.iloc[i,2] < DataForm['dateTimeUTC'].iloc(-1) - duration):
        if(DateForm.iloc[i,2] == start_date):
            while(DataForm.iloc[i,2] <= end_date):
                i++
        else:
            dictindex = DataForm.iloc[i,2]
            while(DataForm.iloc[i,2] < dictindex + duration):
                currentdate = DataForm.iloc[i,2]
                while(DataForm.iloc[i,2] == currentdate):

            sum = 0
            for j in xrange(96):

            i += 96
