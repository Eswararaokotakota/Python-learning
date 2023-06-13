import pandas as pd

data = open("E:\\Coding\\sample_csv_files\\0.0-1.0_2022_03_10_13_20_13_Laser8_L3.csv")
dataa = pd.read_csv(data)
print(dataa.head())#head will prints first 5 rows if we didn'tdefine any nymber

print(dataa.head(10))

#we can printh the last values (starting from last value)
data1 = open("E:\\Coding\\sample_csv_files\\0.0-1.0_2022_03_10_13_20_13_Laser8_L3.csv")
data1 = pd.read_csv(data1)
print(data1.tail())

