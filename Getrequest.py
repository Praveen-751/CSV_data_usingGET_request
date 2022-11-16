import requests,json
import pandas as pd
import csv
import time
import os
filename="users.csv"
fields=['id','Firstname','Lastname','Username','Email','Avatar','Gender','DoB','Address']
rows=[] 
print("enter no of data requests: ",end="")
n=int(input())
for i in range(n): 
    l=[]
    data=requests.get("https://random-data-api.com/api/v2/users")
    data=json.loads(data.content)
    keys=data.keys()
    for i in keys:
        if i=="id":
            id1=data['id']
            id1=str(id1)
        if i=="first_name":
            firstname=(data['first_name'])
        if i=="last_name":
            lastname=(data['last_name'])
        if i=="avatar":
            avatar=(data['avatar'])
        if i=="email":
            email=(data['email'])
        if i=="gender":
            gender=(data['gender']) 
        if i=="username":
            username=(data['username']) 
        if i=="date_of_birth":
            DOB=data['date_of_birth']
        if i=="address":
            city=(data['address']['city'])
            street_add=(data['address']['street_address'])
            street_name=(data['address']['street_name'])
    address=street_name+","+street_add+","+city
    avatar2=''
    for i in avatar:
        if i=='?':
            break
        else:
            avatar2=avatar2+i

    l.append(id1)
    l.append(firstname)
    l.append(lastname)
    l.append(username)
    l.append(email)
    l.append(avatar2)
    l.append(gender)
    l.append(DOB)
    l.append(address)
    rows.append(l)
    time.sleep(1)
if  os. path. getsize(filename) == 0:
    with open(filename, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 

        # writing the fields 
        csvwriter.writerow(fields) 

        # writing the data rows 
        csvwriter.writerows(rows)

else:    
    with open(filename, 'a') as csvfile: 
        csvwriter = csv.writer(csvfile) 

        # writing the data rows 
        csvwriter.writerows(rows)


data = pd.read_csv(filename)
data.to_csv(filename, index=False)
data.head()