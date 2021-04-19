#Import pandas as pd
import pandas as pd

#define importdata function
def importdata(filename):
    data = pd.read_csv(filename)
    print(data.head())
    print(data.index)
    print(data.info)
    return data

importdata("Estimates_of_Disposable_Income_per_Person_2009_2019.csv")

#define cleandata function
def cleandata(filename):
    # validate how many missing values are in the dataset
    data = pd.read_csv(filename)
    missing_value=data.isnull().sum
    print(missing_value)
    #fill missing values with 0
    cleaned_data=data.fillna(method="bfill",axis=0).fillna(0)
    print(cleaned_data)
    return cleaned_data

cleandata("Estimates_of_Disposable_Income_per_Person_2009_2019.csv")

