# importing pandas package
import pandas as pd
import csv,operator

# assign dataset -users.csv
filename="users.csv"
sorted_data= pd.read_csv(filename)
new_sorted="users-sorted.csv"
										
# sort data frame
#sorting with respect to the field Firstname
sorted_data.sort_values(["Firstname"],
					axis=0,
					ascending=[True],
					inplace=True)


if  os. path. getsize(new_sorted) == 0:
    sorted_data.to_csv(new_sorted,index=False)
    data2 = pd.read_csv(new_sorted)
    data2.to_csv(new_sorted, index=False)
else:
    sorted_data.to_csv(new_sorted,index=False)
    data2 = pd.read_csv(new_sorted)
    data2.to_csv(new_sorted, index=False)
data2.head()


