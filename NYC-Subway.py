# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 00:45:41 2015

####################################
# ANALYZING THE NYC SUBWAY DATASET #
####################################

@author: GFR
"""

import numpy as np
import scipy
import scipy.stats
from scipy.stats import ttest_ind
import pandas
import matplotlib.pyplot as plt
import statsmodels.api as sm
import datetime
from ggplot import *

##################
# 1.- Fetch Data #
##################   
weather = pandas.read_csv('turnstile_data_master_with_weather.csv')
days_with_rain = weather['ENTRIESn_hourly'][weather['rain'] == 1]
days_without_rain = weather['ENTRIESn_hourly'][weather['rain'] == 0]

# 2.- Compute Mean and Variance
with_rain_mean = np.mean(days_with_rain)
without_rain_mean = np.mean(days_without_rain)

with_rain_var = np.var(days_with_rain, ddof = days_with_rain.size - 1)
without_rain_var = np.var(days_without_rain, ddof = days_without_rain.size - 1)

print "Hourly entries with rain:    mean = %g, variance = %g" %(with_rain_mean, with_rain_var)#, days_with_rain.size
print "Hourly entries without rain: mean = %g, variance = %g" %(without_rain_mean, without_rain_var)#, days_without_rain.size


##############################
# 3.- Apply statistical test #
##############################
# Welch T Test
# Two sided test. Samples have different variances.
# Null hypothesis: 2 independent samples have identical average (expected) values. 
t, p = ttest_ind(days_with_rain, days_without_rain, equal_var=False)
print "Welch T test: t = %g, two-tail p = %g, one-tail p = %g" % (t, p, p/2)

# Mann Whitney Test
# Can be applied to unkwon distributions
# Null hypothesis: 2 samples come from the same population

U = scipy.stats.mannwhitneyu(weather['ENTRIESn_hourly'][weather['rain'] == 1],weather['ENTRIESn_hourly'][weather['rain'] == 0]).statistic
p = scipy.stats.mannwhitneyu(weather['ENTRIESn_hourly'][weather['rain'] == 1],weather['ENTRIESn_hourly'][weather['rain'] == 0]).pvalue
    
print "Mann Whitney test: U = %g, p = %g" % (U, p)


#########################
# 4.- Linear Regression #
#########################
features = weather[['meanwindspdi','meantempi','precipi','rain', 'Hour','maxtempi']]
dummy_units = pandas.get_dummies(weather['UNIT'], prefix='unit')
features = features.join(dummy_units)
values = weather['ENTRIESn_hourly']

# OLS Method
features = sm.add_constant(features)
model = sm.OLS(values, features)
results = model.fit()
intercept = results.params[0]
params = results.params
    
print "intercept %g" % intercept
print params
#print results.summary()

# Predictions   
predictions = np.dot(features, params)
print predictions

# R squared
DEN = ((weather['ENTRIESn_hourly'] - np.mean(weather['ENTRIESn_hourly']))**2).sum()
NUM = ((predictions - weather['ENTRIESn_hourly'])**2).sum()
    
r_squared = 1 - NUM/DEN

print "R^2 coefficient = %g" % r_squared
print DEN, NUM, r_squared


##################################################################################
# 5.- Visualization of histogram and ridership by time-of-day and by day-of-week #
##################################################################################

# Histrogram
plt.xlabel('ENTRIESn_hourly')
plt.ylabel('Frequency')
plt.title('Histogram of ENTRIESn_hourly')
plt.axis([0, 6000, 0, 45000])
plt.hist([days_without_rain], bins = 200, color = ['blue'], alpha = 1, label = "No Rain")
plt.hist([days_with_rain], bins = 200, color = ['yellow'], alpha = 1, label = "Rain")
plt.legend()

# Ridership by day-of-week
dom = weather[['DATEn', 'ENTRIESn_hourly']].groupby('DATEn', as_index = False).sum()
dom['Day'] = [datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%w %A') for x in dom['DATEn']]
day = dom[['ENTRIESn_hourly', 'Day']].groupby('Day', as_index = False).sum()
ggplot(day, aes(x='Day', y='ENTRIESn_hourly')) + geom_bar(aes(weight='ENTRIESn_hourly'), fill='orange') + ggtitle('NYC Subway Ridership By Day of Week') + xlab('Day') + ylab('Entries')

# Ridership by day-of-month
dom['DAY'] = [x[len(x)-2:len(x)] for x in dom['DATEn']] 
ggplot(dom, aes(x='DAY', y='ENTRIESn_hourly')) + geom_bar(aes(weight='ENTRIESn_hourly'), fill='blue') + ggtitle('NYC Subway Ridership By Day of Month') + xlab('Date') + ylab('Entries')

# Ridership by time-of-day
weather['HOUR'] = [x[0:2] for x in weather['TIMEn']]
day_time = weather[['HOUR', 'ENTRIESn_hourly']].groupby('HOUR', as_index = False).sum()
ggplot(day_time, aes(x='HOUR', y='ENTRIESn_hourly')) + geom_bar(aes(weight='ENTRIESn_hourly'), fill='blue') + ggtitle('NYC Subway Ridership By Time of Day') + xlab('Hour') + ylab('Entries')
