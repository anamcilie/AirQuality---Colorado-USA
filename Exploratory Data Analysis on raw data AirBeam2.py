
"""
Spyder Editor

@author anamcile

Data processing-analysis for the Airbeam2 monitors, in Colorado State

"""

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
path = r'D:\Dropbox\Dropbox\A_CESEP Ana Ilie\Data Science AQ\CSM AQ\DATA\AirBeam2 data'
data = pd.read_csv(path + '/boulder_-_cu_-_2102_boulder_115070__20221004-2875-s9delg.csv')

# Exploratory Data Analysis

data.dtypes # find the datatypes of all variables
data.columns # list of all column names - original list
data.shape # Dimensions of original dataset (rows, columns)
print(data.head(10)) # first 10 rows of dataset
data.index # index - number of rows and columns
data.info() # information on datatypes and number of elements

# rename columns from default values
data.columns = ["ObjectID", "Session_Name", "Timestamp", "Latitude", "Longitude", "PM-2.5"]
data = data.drop('ObjectID', axis=1)

data = data.iloc[8:] # removing the first 7 blank rows and header
data = data.reset_index(drop=True) # resetting the index to start from 0 and not creating a new column

# Convert the datatype of certain columns to float type 
data[['PM-2.5']] = data[['PM-2.5']].apply(pd.to_numeric)

# Convert the timestamp to right format and datetime object
data['Timestamp'] = data['Timestamp'].str.replace('T',' ').str.replace(' ',' ')
# Timestamp needs to be converted to datetime object (for time series manipulations)
data['Timestamp'] = pd.to_datetime(data['Timestamp'])


# Missing Value Analysis
# list number of missing values for each column
print (data.isnull().sum())
null_counts = data.isnull().sum()


# replacing all the zeros with NaN
#data = data[data.columns].replace(0, np.nan)
# dropping all the rows with NaN in the columns 
data.dropna(inplace=True)
# recheck the shape of dataframe if values changed
data.shape

# save the cleaned data file to another .csv, in the same folder
data.to_csv(path + "\Cleaned_Data_File_boulder_-_cu.csv")


# store descriptive statistics in a different dataframe and .csv file
desc_stat = data.describe()
desc_stat.to_csv(path+'\Descriptive_Stats_boulder_-_cu.csv')

# see the results of desired column
print (desc_stat['PM-2.5'])




# Run following 6 lines together for plot
plt.figure(figsize=(14,8))
plt.xticks(np.arange(len(null_counts)), null_counts.index, rotation='vertical')
plt.xlabel('Columns')
plt.ylabel('Number of Attributes with Missing Data')
plt.bar(np.arange(len(null_counts)), null_counts)
plt.title('Missing Value Analysis')


# Continous Variables in the dataset
data_cont = data.iloc[:,:].reset_index() 
data_cont = data_cont.drop(['index'], axis = 1)
data_cont.shape
data_cont.columns

# Boxplot Analysis to see presence of outliers
sns.boxplot(y=data_cont["PM-2.5"], data=data)


# Basic Plots

data_cont.boxplot()
#plt.savefig(path + "\boxplot_boulder_-_cu.jpg")


# Line Plot - continous variables
pm_conc = ['PM-2.5']
plt.plot(data_cont[pm_conc])
plt.xlabel('Timestamp')
plt.ylabel('PM Concentration')
plt.show()
plt.savefig(path + "\Line Plot_boulder_-_cu.jpg")


# Histogram
data_cont.hist("PM-2.5", figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)

# Distribution Plot
plt.figure(figsize=(20,10))
sns.distplot(data_cont['PM-2.5'], label='PM-2.5')
plt.xlabel('Variable Estimate')
plt.title('Distribution Plot - Kernel Density Estimate')
plt.legend()


# Time Series Analysis
data2 = data.set_index('Timestamp')
data2.head(3)

data2['Month'] = data2.index.month
data2['Year'] = data2.index.year
#data2['Weekday Name'] = data2.index.weekday_name
data2.sample(5, random_state = 0)
# time slicing
data_March = data2.loc['2020-03-01':'2021-03-01'] # March Data
data_March2 = data2.loc['2020-03']  

data_March['PM-2.5'].plot(linewidth = 0.5)

cols_plot = ['PM-2.5']
axes = data_March[cols_plot].plot(marker='.', alpha=0.5, linestyle='None', figsize=(11, 9), subplots=True)
for ax in axes:
    ax.set_ylabel('PM2.5 ug/m3')

# slicing and plotting at the same time
data2.loc['2020-03-2 15:00:00':'2020-03-31 20:30:00', 'PM-2.5'].plot()

# number of observations per timestamp
data2.groupby(level=0).count()

# mean values on a daily basis
data2.resample('D').mean()


data.index = pd.to_datetime(data.index)

data.resample('D').mean()
data.to_csv(path + "\Daily avg_boulder_-_cu.csv")




