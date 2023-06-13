from ast import Index
import pandas as pd

file = open("E:\\Coding\\Python\\Training\\task_1\\employe_data.csv", "r")

data = pd.read_csv(file) #reading as dataframe  

print(data)

data1 = data[ (data['Age']>24) & (data['Age']<30) ]

# file = open("E:\\Coding\\Python\\Training\\task_2\\filtered_age.csv", "w")

data1.to_csv("E:\\Coding\\Python\\Training\\task_2\\filtered_age.csv",index=False)

print(data1)