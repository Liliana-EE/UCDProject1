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

# Start the process by importind and cleaning datasets that will be used for the report
# Import & clean Housing stock table
importdata("Housing_in_Ireland_per_County.csv")
cleaned_df1=cleandata("Housing_in_Ireland_per_County.csv")

# Import & clean Commencement Notices table
importdata("Commencement_Notices_per_County.csv")
cleaned_df2=cleandata("Commencement_Notices_per_County.csv")

# Import & clean table of Estimate of disposable Income per Person by region
importdata("Estimates_of_Disposable_Income_per_Person_2009_2019.csv")
cleaned_df3=cleandata("Estimates_of_Disposable_Income_per_Person_2009_2019.csv")

# Import table of Stores list for discounters 2021
cleaned_df4=importdata("Stores_list_v2021.csv")

# Import table of Population in Ireland by demographics in 2016
importdata("SAPS2016_IE_Population_Family_Size_and_Internet_Acess.csv")
cleaned_df5=cleandata("SAPS2016_IE_Population_Family_Size_and_Internet_Acess.csv")

# Import table of Population in Ireland by industries and other demographics in 2016
cleaned_df6=importdata("Workplace_zones_SAPS_2016_M.csv")

#Merge Housing stock table, Estimate of Disposable Income table and Commencement Notices table

#In order to find the total number of residential Commencement Notices have been authorised
# during the pandemic by region in the ROI

#Convert cleaned_df1, cleaned_df2 and cleaned_df3 tables to conver from year
# 2016 to 2020 columns into rows

def convertdata(filename):
    # validate how many missing values are in the dataset
    data = pd.read_csv(filename)
    cleaned_df1 = cleandata(data1)
    cleaned_df1_year =(cleaned_df1.set_index(["County","Region","Subregion"])
               .stack()
               .reset_index(name="Value")
               .rename(columns={"2016","2017","2018","2019","2020"}))
    print(cleaned_df1_year.head())
    data = pd.read_csv(filename)
    cleaned_df2 = cleandata(data1)
    cleaned_df2_year = (cleaned_df2.set_index(["County", "Region", "Subregion"])
                        .stack()
                        .reset_index(name="Value")
                        .rename(columns={"2016", "2017", "2018", "2019", "2020"}))
    print(cleaned_df2_year.head())


