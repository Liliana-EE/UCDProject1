# Import pandas as pd
import numpy as np
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

#Merge po and stores on subregion and county with fill and
pop= cleandata("Pop_2016.csv")
stores = cleandata("Stores.csv")

#pop_stores = pd.merge_ordered(pop,stores,on=["subregion","county"],
#                              fill_method="ffill")
#print(pop_stores)

#Total_pop = pivot_table(pop, values=["Total population"]),\
#          rows=["Subregion"],cols= [["Region"], aggfunc] = np.sum, margins=True)
#Total_pop.stack("Region")

print(pop.append(pop[["Total Population"]].sum().rename('Gran Total')).fillna(""))

#pop.loc["Gran Total"] = pop[["Total Population"]].sum()
#pop.loc["Gran Total"] = pop.loc["Total Population"].fillna("")

#for label, _pop in pop.groupby(["Total Population"]):
#    print(label)
#   print(_pop)
#    print()

print(type(pop))

#pop.column.dtypes

import pandas as pd
#df = pd.DataFrame({"Total Population"})

#fig, ax = plt.subplots()
#plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

df= importdata("Housing_vs_Comm_Notices.csv")

sns.barplot(x="Year",  y="Value",  hue="Subregion",
 data=df)

plt.show()