# Import pandas as pd
import pandas as pd

# define importdata function
def importdata(filename):
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

cleandata("Housing_vs_Comm_Notices.csv")
cleandata("Stores_list_v2021.csv")

# Merge the Housing_vs_Comm_Notices and store_list tables and taxi_veh tables
hou_cn_df = cleandata("Housing_vs_Comm_Notices.csv")
stores_df = cleandata("Stores_list_v2021.csv")
hou_cn_stores = hou_cn_df.merge(stores_df, on="County")
print(hou_cn_stores.head())

# Print the column names of the taxi_own_veh
print(hou_cn_stores.columns)
