# Import pandas as pd
import numpy as np
import pandas as pd


# define importdata function
def importdata(filename):
    data = pd.read_csv(filename)
    print(data.head())
    print(data.index)
    print(data.info)
    missing_values = data.isnull().sum
    print(missing_values)
    cleaned_data = data.fillna(method="bfill", axis=0).fillna(0)
    print(cleaned_data)
    return cleaned_data

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



pop= importdata("Pop_2016.csv")
hous_cnot = importdata("Housing_vs_Comm_Notices.csv")
stores = importdata("Stores_No..csv")


pop_subregion = pivot_table(pop, values=["Population No."], cols=["Subregion"], aggfunc=np.cumsum(), margins=True)
pop_subregion.stack("Subregion")

