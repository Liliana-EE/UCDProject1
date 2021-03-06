import pandas as pd

# 1. Importing using Pandas
# 2. Clean dataset defined
# 3. Join population and stores tables by Region and Subregion
# and get the number of population and stores per subregion
# Consider columns County, Region, Subregion and filter_criteria Sub regions
# Border, Dublin, Mid East, Mid West, Midland, South East, South West, West

# 1st attempt of merging with three tables
from numpy.core import sort


def joindata(filename):
    data1 = pd.read_csv(filename)
    cleaned_df1 = cleandata(data1)
    data2 = pd.read_csv(filename)
    cleaned_df2 = cleandata(data2)
    # compile the list of dataframes you want to merge
    data_1_2 = [cleaned_df1, cleaned_df2]
    # merge multiple tables based on different column names and call it altered_data
    data_merged = cleaned_df1.merge(cleaned_df2, on=["Region", "Subregion"])
    # group the results by "column name" and find the median value
    Sub_region_median = data_merged.groupby("Subregion", as_index=False).agg([{"value": "median"}])
    # sort group_median and print the results
    sorted_group_median = group_median.sort_values(["_hou", "_CN", "_DIn"], ascending=[True, True, True])
    # print the results
    print(sorted_group_median.head())


# 2nd attempt:  Merge pop and stores on subregion and county
# pop= cleandata("Pop_2016.csv")
# stores = cleandata("Stores_No.csv")
# hou_cn = cleandata("Housing_vs_Comm_Notices.csv")
# pop_stores = pd.merge_ordered(pop,stores,on=["subregion","county"],
#                              fill_method="ffill")
# print(pop_stores)


# 3rd attempt: merging
# pop = importdata("Pop_2016.csv")
# stores = importdata("Stores_No..csv")
# pop_stores = pop.merge(stores, on="Subregion")
# pop_stores_gruped = pop_stores.groupby(["Population No.","Aldi","Lidl"],as_index=False).agg({"Subregion":"count"})
# print(sorted_pop_stores_grouped = pop_stores_gruped.sort_values(["Population No.","Aldi","Lidl"],ascending=([False,False,True]))


# 4. From pop_stores tables to group # of stores by Sub region and create new column
# named "% Coverage_Opp" containing the difference between stores and population
# by discounter criteria factor of 10,000

# pop_subregion = pivot_table(pop, values=["Population No."], cols=["Subregion"], aggfunc=np.cumsum(), margins=True)
# pop_subregion.stack("Subregion")


# 5. Plot "% Coverage_Opp" and date by sub region
# 5.1 Create a figure and plot Total Populations against the Year
import matplotlib.pyplot as plt


# fig, ax=plt.subplots()
# ax.plt(hou_cn["Year"], hou_cn["Subregion"])
# ax.set_title("housing stock vs commencement notices")
# plt.show()

#def importdata(param):
#    def importdata(filename):
#        data = pd.read_csv(filename)
#        print(data.head())
#        print(data.index)
#        print(data.info)

    #return data


#data = importdata("Housing_vs_Comm_Notices.csv")

#import seaborn as sns

#sns.barplot(x="Year", y="Value", hue="Subregion", data=data)
#plt.title("Housing_or_CommNotices")
#plt.show()

pop = importdata("Pop_2016.csv")

Total_pop = pivot_table(pop, values=["Total population"]),\
          rows=["Subregion"],cols= [["Region"], aggfunc] = np.sum, margins=True)
 Total_pop.stack("Region")

print(pop.append(pop[["Total Population"]].sum().rename('Gran Total')).fillna(""))

pop.loc["Gran Total"] = pop[["Total Population"]].sum()
pop.loc["Gran Total"] = pop.loc["Total Population"].fillna("")

# for label, _pop in pop.groupby(["Total Population"]):
#   print(label)
#   print(_pop)
#   print()

# print(type(pop))

# pop.column.dtypes

# df = pd.DataFrame({"Total Population"})

# Attempt#
# Create a DataFrame from csv file
# housing_cnot_date = importdata("Housing_Comm_Notices_1co.csv")
# PCT_Change_C.Notices = housing_cnot_date["PCT_Change C.Notices"]

# Create line plot
# g = sns.lineplot(x="date", y="PCT_Change_C.Notices",
#                 data=housing_cnot_date,
#                 hue="origin")

# Add a title "Average MPG Over Time"
# g.set_title("Growth Rate of Commencement Notices")

# Show plot
# plt.show()

# Attempt#
# ax.scatter(c_notices["No. of households"], pop_stores["Stores"], c=pop_stores.index)

# Set the x-axis label to "Population"
# ax.set_xlabel("Population")
# Set the y-axis label to "Stores"
# ax.set_ylabel("Stores")

# plt.show()
