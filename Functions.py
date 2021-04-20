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
pop_stores = importdata("pop_stores.csv")
housing_cnot_date = importdata("Housing_Comm_Notices_1co.csv")



#Making a count plot with a list
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame from csv file
stores_con = importdata("Stores_con.csv")
Subregion = stores_con["Subregion"]

# Create bar plot with subregion on the y-axis
sns.countplot(y=Subregion)

# Add title
plt.title("Stores per region")

# Show plot
plt.show()

# Create a DataFrame from csv file
#housing_cnot_date = importdata("Housing_Comm_Notices_1co.csv")
#PCT_Change_C.Notices = housing_cnot_date["PCT_Change C.Notices"]

# Create line plot
#g = sns.lineplot(x="date", y="PCT_Change_C.Notices",
#                 data=housing_cnot_date,
#                 hue="origin")

# Add a title "Average MPG Over Time"
#g.set_title("Growth Rate of Commencement Notices")

# Show plot
#plt.show()


#matplotlib inline
import pandas as pd
import matplotlib as mpl

df = importdata("Housing_n_CN_YCol.csv")

df.plot(y = ['2016','2017','2018','2017','2018'], x='Subregion')

df.plot()
plt.show()


c_notices = importdata("Housing_Comm_Notices_1co.csv")

# Display a scatter plot using color
fig, ax = plt.subplots()
plt.show()

ax.scatter(c_notices["No. of households"], pop_stores["Stores"], c=pop_stores.index)

# Set the x-axis label to "Population"
ax.set_xlabel("Population")
# Set the y-axis label to "Stores"
ax.set_ylabel("Stores")

plt.show()

