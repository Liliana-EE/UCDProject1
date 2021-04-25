# Import pandas as pd
import numpy as np
import pandas as pd


# define importdata function
def importdata(filename):
    data1 = pd.read_csv(filename)
    print(data1.head())
    print(data1.describe)
    print(data1.info)
    print(data1.shape)
    data1['Date'] = pd.to_datetime(data1['Date'])
    data1['Year'] = data1['Date'].dt.year  # getting year
    data1['Month'] = data1['Date'].dt.month  # getting month
    data1['Day'] = data1['Date'].dt.day  # getting day


data1 = importdata('supermarket_sales - Sheet1.csv')


# define cleandata function
def cleandata(filename):
    # validate how many missing values are in the dataset
    data1 = pd.read_csv(filename)
    # define missing_values
    missing_values = data1.isnull().sum
    print(missing_values)
    # fill missing values with 0
    cleaned_data = data1.fillna(method="bfill", axis=0).fillna(0)
    print(cleaned_data)
    return cleaned_data


City = data1['City']
Gender = data1['Gender']

print(City.head())

# sort data1 by city, then descending gender
data1_cit_gen = data1.sort_values(['City', 'Gender'], ascending=[True, False])
print(data1_cit_gen.head())
