import pandas as pd

# To read a json file we need a json file
a = pd.read_json("E:\Coding\Python\Pandas\sample.json")
print(a)
'''print(a.to_string)'''#they said it will prints the entire data but even without this command it is printing entire data

#WE CAN WRITE JSON FILE IN DISTONORY, IN THAT CASE
#if we have json data in our python code as distonory then we can directly print the data using pd.dataframe()
