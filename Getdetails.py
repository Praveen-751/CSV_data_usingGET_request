from pandas import *
import csv
print("enter the id to print details:",end=" ")
inputid=int(input())
filename="Useres.csv"
data=read_csv(filename)
id1=data['id'].to_list()
count=0
for i in id1:
    if i==inputid:
        count=count+1
    
if count==1:
    with open (filename, "r") as source:
        reader = csv.reader(source)
        data = []
        for row in reader:
            data.append(row)
        for i in range(1,len(data),2):
            if data[i][0]==str(inputid):
                for j in range(9):
                    print(data[i][j],end=" ")
else:
    print("No data found" )