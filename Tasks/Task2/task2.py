
#Read the values whose the age is >24 and <30 using pandas

import pandas as pd

file = open("E:\\Coding\\Python\\Tasks\\Task_1\\employe_data.csv", "r")

data = pd.read_csv(file) #reading as dataframe  

print(data)

data1 = data[ (data['Age']>24) &(data['Age']<30) ]

print(data1)

print("------------------Task-1 completed-----------------")

# file1 =open("E:\\Coding\\Python\\tasks\\Task_1\\employe_data.csv", "w")
# file2 = open("E:\\Coding\\Python\\tasks\\Task2\\modified_employe_data.csv","w")
data1.to_csv("E:\\Coding\\Python\\Tasks\\Task2\\modified_employe_data.csv",index=False)

print("----------------------Done Writing---------------")