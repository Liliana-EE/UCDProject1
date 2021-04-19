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
def joindata (filename):
    data1 = pd.read_csv(filename)
    cleaned_df1 = cleandata(data1)
    data2 = pd.read_csv(filename)
    cleaned_df2 = cleandata(data2)
    data3 = pd.read_csv(filename)
    cleaned_df3 = cleandata(data3)
    # compile the list of dataframes you want to merge
    data_frames = [cleaned_df1, cleaned_df2, cleaned_df3]
    #merge multiple tables based on different column names and call it altered_data
    data_merged = cleaned_df1.merge(cleaned_df2,on=["Region","Sub region"]) \
        .merge(cleaned_df3, on="sub region", suffixes=("_hou","_CN","_DInc"))
    #group the results by "column name" and find the median value
    Sub_region_median = data_merged.groupby("Sub region", as_index=False).agg([{"value":"median"}])
    #sort group_median and print the results
    sorted_group_median = group_median.sort_values(["_hou","_CN","_DIn"], ascending=[True,True,True])
    #print the results
    print(sorted_group_median.head())

#Start the process by importind and cleaning datasets that will be used for the report
#Import & clean Housing stock table
importdata("Housing_in_Ireland_per_County.csv")
cleandata("Housing_in_Ireland_per_County.csv")

#Import & clean Commencement Notices table
importdata("Commencement_Notices_per_County.csv")
cleandata("Commencement_Notices_per_County.csv")

