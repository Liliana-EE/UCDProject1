import pandas as pd


# 1. Importing using Pandas

# 2. Clean dataset defined


# 3. Join population and stores tables by County, Region and Subregion
# and get the number of population and stores per subregion
# Consider columns County, Region, Subregion and filter_criteria Sub regions
# Border, Dublin, Mid East, Mid West, Midland, South East, South West, West


#1st attempt of merging with three tables
#def joindata (filename):
    #data1 = pd.read_csv(filename)
    #cleaned_df1 = cleandata(data1)
    #data2 = pd.read_csv(filename)
    #cleaned_df2 = cleandata(data2)
    # compile the list of dataframes you want to merge
    #data_1_2 = [cleaned_df1, cleaned_df2, cleaned_df3]
    #merge multiple tables based on different column names and call it altered_data
    #data_merged = cleaned_df1.merge(cleaned_df2,on=["Region","Sub region"]) \
        #.merge(cleaned_df3, on="sub region", suffixes=("_hou","_CN","_DInc"))
    #group the results by "column name" and find the median value
    #Sub_region_median = data_merged.groupby("Sub region", as_index=False).agg([{"value":"median"}])
    #sort group_median and print the results
    #sorted_group_median = group_median.sort_values(["_hou","_CN","_DIn"], ascending=[True,True,True])
    #print the results
    #print(sorted_group_median.head())


#2nd attempt:  Merge pop and stores on subregion and county
# pop= cleandata("Pop_2016.csv")
# stores = cleandata("Stores_No.csv")
# hou_cn = cleandata("Housing_vs_Comm_Notices.csv")
# pop_stores = pd.merge_ordered(pop,stores,on=["subregion","county"],
#                              fill_method="ffill")
# print(pop_stores)


# 3rd attempt: merging
#pop = importdata("Pop_2016.csv")
#stores = importdata("Stores_No..csv")
#pop_stores = pop.merge(stores, on="Subregion")
#pop_stores_gruped = pop_stores.groupby(["Population No.","Aldi","Lidl"],as_index=False).agg({"Subregion":"count"})
#print(sorted_pop_stores_grouped = pop_stores_gruped.sort_values(["Population No.","Aldi","Lidl"],ascending=([False,False,True]))


# 4. From pop_stores tables to group # of stores by Sub region and create new column
# named "% Coverage_Opp" containing the difference between stores and population
# by discounter criteria factor of 10,000


# 5. Plot "% Coverage_Opp" and date by sub region
# 5.1 Create a figure and plot Total Populations against the Year
#import matplotlib.pyplot as plt
# fig, ax=plt.subplots()
# ax.plt(hou_cn["Year"], hou_cn["Subregion"])
# ax.set_title("housing stock vs commencement notices")
# plt.show()

#df = importdata("Housing_vs_Comm_Notices.csv")

#import seaborn as sns
#sns.barplot(x="Year", y="Value", hue="Subregion", data=df)
#plt.title("Housing_or_CommNotices")
#plt.show()


# Total_pop = pivot_table(pop, values=["Total population"]),\
#          rows=["Subregion"],cols= [["Region"], aggfunc] = np.sum, margins=True)
# Total_pop.stack("Region")

# print(pop.append(pop[["Total Population"]].sum().rename('Gran Total')).fillna(""))

# pop.loc["Gran Total"] = pop[["Total Population"]].sum()
# pop.loc["Gran Total"] = pop.loc["Total Population"].fillna("")

# for label, _pop in pop.groupby(["Total Population"]):
#   print(label)
#   print(_pop)
#   print()

# print(type(pop))

# pop.column.dtypes

#df = pd.DataFrame({"Total Population"})

