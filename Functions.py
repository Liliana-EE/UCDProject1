# Import pandas as pd
import numpy as np
import pandas as pd


# define importdata function
def importdata(filename) -> object:
    data = pd.read_csv(filename)
    print(data.head())
    print(data.index)
    print(data.info)
    return data


# define cleandata function
def cleandata(filename):
    # validate how many missing values are in the dataset
    data = pd.read_csv(filename)
    # define missing_values
    missing_values = data.isnull().sum
    print(missing_values)
    # fill missing values with 0
    cleaned_data = data.fillna(method="bfill", axis=0).fillna(0)
    print(cleaned_data)
    return cleaned_data

# Initialize offset
offset = -6
# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset = offset - 1
    else:
      offset = offset + 1
    print(offset)

print(importdata("Pop_2016.csv").pop)
print([pop["Subregion"]])