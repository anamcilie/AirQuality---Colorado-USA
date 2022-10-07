# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 22:18:25 2022

@author: anamc
"""

def time_variation(df, pollutant, ylabel, hue=None):
     # importing all the libraries we'll need
     import pandas as pd
     import numpy as np
     import seaborn as sns
     import matplotlib.pyplot as plt
     
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime
from pandas import Series        # To work on series
import statsmodels
import warnings                   # To ignore the warnings
warnings.filterwarnings("ignore")
import seaborn as sns
sns.set_style("white")
plt.style.use("seaborn")
# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(14, 8)})

# sns.set() # setting to default settings
# plt.rcParams # set default matplotlib settings


# finding the current directory
abs_path = os.getcwd()
abs_path

# change to desired folder where .csv file is present - Use forward backslash
path = r'D:\Dropbox\Dropbox\A_CESEP Ana Ilie\Data Science AQ\CSM AQ\DATA IQAirVisual'
data = pd.read_csv(path + '/May 2022 October 16th 2022.csv')

# Exploratory Data Analysis

data.dtypes # find the datatypes of all variables
data.columns # list of all column names - original list
data.shape # Dimensions of original dataset (rows, columns)
print(data.head(10)) # first 10 rows of dataset
data.index # index - number of rows and columns
data.info() # information on datatypes and number of elements

# Convert the datatype of certain columns to float type 
data[['Datetime']] = data[['Datetime']].apply(pd.to_datetime)
# Convert the datatype of certain columns to float type 
data[['PM2.5 (ug/m3)']] = data[['PM2.5 (ug/m3)']].apply(pd.to_numeric)
    
#setting xticklabels
week = ['mon','tue','wed','thu','fri','sat','sun']
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

data.info() # information on datatypes and number of elements


# Creating graphs of pollutant concentrations by hour, month and day of week
fig,axes = plt.subplots(1, 3,sharex=False, figsize=(16,4)) #creating subplots, side by side
fig.tight_layout(pad=2) # makeing plots get closer
sns.set_style('whitegrid')

# concentration vs hour
axes[0] = sns.lineplot(ax=axes[0],data=data,
                            x=data['Datetime'].dt.hour,
                            y=data['PM2.5 (ug/m3)'],
                            color='red',
                            linewidth=1.5,
                            palette="hls")
axes[0].set_xticklabels(axes[0].get_xticks(), fontsize=13)
axes[0].set_yticklabels(axes[0].get_yticks(), fontsize=13)
axes[0].set_xlabel('hour', fontsize=13)
axes[0].set_ylabel('PM2.5 ug/m3', fontsize=13)
axes[0].legend().set_title('CSM')

    # concentration vs month
axes[1] = sns.lineplot(ax=axes[1],
                           data=data,
                           x=data['Datetime'].dt.month,
                           y=data['PM2.5 (ug/m3)'],
                           color='red',
                           linewidth=1.5,
                           palette="hls")
axes[1].set_xticks(np.arange(1, 13, 1))
axes[1].set_xticklabels(months, fontsize=13)
axes[1].set_yticklabels('')
axes[1].set_xlabel('month', fontsize=13)
axes[1].set_ylabel('PM2.5 ug/m3')
axes[1].legend().set_title('CSM')

    # concentration vs day of week
axes[2] = sns.lineplot(ax=axes[2],
                           data=data,
                           x=data['Datetime'].dt.dayofweek,
                           y=data['PM2.5 (ug/m3)'],
                           color='red',
                           linewidth=1.5,
                           palette="hls")
axes[2].set_xticks(np.arange(0, 7, 1))
axes[2].set_xticklabels(week, fontsize=13)
axes[2].set_yticklabels('')
axes[2].set_xlabel('day of week', fontsize=13)
axes[2].set_ylabel('')
axes[2].legend().set_title('CSM')
    
    
    

    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     