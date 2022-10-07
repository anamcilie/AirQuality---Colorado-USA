# -*- coding: utf-8 -*-
"""
Spyder Editor

@ anamcilie
Data analysis for the IQ Air Visual Monitor 

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime
from pandas import Series        
import statsmodels
import warnings                   
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



############### Time Series ###################

# Line Plot - continous variables
#pm_conc = ['PM-1','PM-10','PM-2.5']
# Set the Date as Index
data['Datetime'] = pd.to_datetime(data['Datetime'])
data.index = data['Datetime']
del data['Datetime']
pm_conc = ['PM2.5 (ug/m3)']
plt.plot(data[pm_conc])
plt.xlabel('Datetime')
plt.ylabel('PM2.5 (ug/m3)')
plt.show()
plt.savefig(path + "\Timeseries_May 2022 October 16th 2022.jpg")
    


# Missing Value Analysis
# list number of missing values for each column
print (data.isnull().sum())
null_counts = data.isnull().sum()

# Run following 6 lines together for plot
plt.figure(figsize=(5,8))
plt.xticks(np.arange(len(null_counts)), null_counts.index, rotation='vertical')
plt.xlabel('Columns')
plt.ylabel('Number of Attributes with Missing Data')
plt.bar(np.arange(len(null_counts)), null_counts)
plt.title('Missing Value Analysis')
plt.savefig(path + "\Missing Value Analysis_CSM.jpg")


# replacing all the zeros with NaN
#data = data[data.columns].replace(0, np.nan)
# dropping all the rows with NaN in the columns 
#data.dropna(inplace=True)
# recheck the shape of dataframe if values changed
data.shape

# save the cleaned data file to another .csv, in the same folder
#data.to_csv(path + "\Cleaned_Data_File_May 2022 October 16th 2022.csv")


# store descriptive statistics in a different dataframe and .csv file
desc_stat = data.describe()
desc_stat.to_csv(path+'\Descriptive_Stats_May 2022 October 16th 2022.csv')



# Basic Plots

data.boxplot()
plt.savefig(path + "\Boxplots_.jpg")

# Pair Plot
#sns.pairplot(data)
#plt.savefig(path + "\pairplot.jpg")


# Histogram
data.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8)
plt.savefig(path + "\Histogram.jpg")

# Distribution Plot
plt.figure(figsize=(20,10))
sns.distplot(data['PM2.5 (ug/m3)'], label='PM2.5 ug/m3')
plt.xlabel('Variable Estimate')
plt.title('Distribution Plot - Kernel Density Estimate')
plt.legend()
plt.savefig(path + "\Distribution Plot.jpg")


# mean values on a daily basis
#data.resample('D').mean()
#data.to_csv(path + "\Daily avg_CSM.csv")

























