import pandas as pd

file = pd.read_csv("E:\\Coding\\Python\\Pandas\\clean_data.csv")
#Remove all rows with NULL values:
file.dropna(inplace = True)
print(file.to_string()) #will removers the empty cells

#we can fill the empty cells with our defined valuesusing fillna() method

file1 = pd.read_csv("E:\\Coding\\Python\\Pandas\\clean_data.csv")
file1.fillna(14,inplace=True)
print(file1)#will fills the empty cells

