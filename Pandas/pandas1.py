import pandas as pd

#here is how to check the pandas version
print(pd.__version__)

#example code to know how pandas will work
my_data = {
"names": ["eswar","tanooj","gali"],
"age" : [21,22,"3 years"]
}
movedhere =pd.DataFrame(my_data)
print(movedhere) #it will prints the data assigned with number and makes a tabular form

# SERIES IN PANDAS
a = [3,4,5,6]#here in this code no labels are specified like the names above hence it will assign the index numbers as labels
data = pd.Series(a)
print(data) #It will prints the data by assigning the numbers one by one 
#we can call the data with the index number also
print(data[1:])

#we can give labels by using the index argument
b = [9,8,7]
data1 = pd.Series(b,index=["x","y","z"]) #it will assign the names x,y,z to the respective index values of data1
print(data1)
print(data1["z"]) #we can access the data by the label also
#we can also access the key/values like distonories
c = {"eswar":"enginner","rao":"student","age":21}
data2 = pd.Series(c) #it will take the values to the respected key and displays as pandas result format
print(data2)

#we can specify the data range to get the data from the distonory by the index values
c = {"eswar":"enginner", "rao":"student", "age":21, "town":"bhimavaram", "graduation":"Btech", "learning":"python"}
data3 = pd.Series(c,index = ["rao","graduation"])# it will gives you the values between the range of index values you given
print(data3)

#DATA FRAMES
data3 = {
    "names" : ["eswar","rao","kottakota",72],
    "graduation" : ["btech","diploma","life",66],
    "job" : ["engineer","embedded","vlsi",86]
}
data = pd.DataFrame(data3) #Data frame takes two dimentional data
print(data)
#we can olocate a specified row using loc orgument in python
print(data.loc[1])
#wecan print the index values toandfrom using loc
print(data.loc[[0,2]])


#we can give a name for each row using index
data4 = {
    "names" : ["eswar","rao","kottakota",72],
    "graduation" : ["btech","diploma","life",66],
    "job" : ["engineer","embedded","vlsi",86],
    "python": ["list","csv","pandas","learning"]
}
data = pd.DataFrame(data4,index=["day1","day2","day3","day4"])
print(data)
#we can also locate the row with the specified name also
print(data.loc["day2"])