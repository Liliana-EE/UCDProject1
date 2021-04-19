#Import pandas as pd
import pandas as pd

#define importdata function
def importdata(filename):
    data = pd.read_csv(filename)
    print(data.head())
    print(data.index)
    print(data.info)
    return data


#define cleandata function
def cleandata(filename):
    # validate how many missing values are in the dataset
    data = pd.read_csv(filename)
    #define missing_values
    missing_values=data.isnull().sum
    print(missing_values)
    #fill missing values with 0
    cleaned_data=data.fillna(method="bfill",axis=0).fillna(0)
    print(cleaned_data)
    return cleaned_data

#define joindata function
def joindata (filename)
    data = cleandata(filename)
    #merge X and Y tables on "column name" called altered_data
    altered_data = data.merge(filename,on="column")
    #group the results by "column name" then count the number of elements


