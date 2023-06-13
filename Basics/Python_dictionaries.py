#distonories in python are ordered, changable, BUt do not allows the duplicate values
# key : value

from typing import ItemsView


dict1 = {
    "key" : "value",
    "name" : "eswar",
    "age" : 21,
    "pin" : 413,
    "married" : False
    }
print(dict1)

#we can access the value by calling key
dict2 = {
    "key" : "value",
    "name" : "eswar",
    "age" : 21,
    "pin" : 413,
    "married" : False,
    "method" : "access"
    }
x = dict2["name"]
print(x)
print(dict2["married"])

#we can access the keys in the distonary easily by using "key" method
dict3 = {
    "key" : "value",
    "name" : "eswar",
    "age" : 21,
    "pin" : 413,
    "married" : False,
    "method" : "access all keys"
    }
x = dict3.keys()
print(x)

#We can get only values from distonary
dict5 = {
    "key" : "value",
    "name" : "eswar",
    "age" : 21,
    "pin" : 413,
    "married" : False
    }
x = dict5.values()
print(x)

#We can change a value of a key later
dict6 = {
    "key" : "value",
    "name" : "eswar",
    "age" : 21,
    "pin" : 413,
    "married" : False
    }
dict6["name"] = "eswararao"
print(dict6)

#We can add extra key:value in dictonory
dict7 = {
    "key" : "value",
    "name" : "eswar",
    "age" : 21,
    "pin" : 413,
    "married" : False
    }
dict7["branch"] = "ECE"
print(dict7)

#We can use update() method to update items
dict7 = {
    "key" : "value",
    "name" : "eswar",
    "age" : 21,
    "pin" : 413,
    "married" : False
    }
dict7.update({"pin":"199P5A0413"})
print(dict7)


#To get distnory key:values as list format we use items() method
dict8 = {
    "key" : "value",
    "name" : "eswar",
    "age" : 21,
    "pin" : 413,
    "married" : False
    }
x =dict8.items()
print(x)


#We can confirm if any key u want is existed in distonory or not
dict9 = {
    "key" : "value",
    "name" : "eswar",
    "age" : 21,
    "pin" : 413,
    "married" : False
    }
if "pin" in dict9:
    print("yout pin is: ", "pin")


#REMOVING ITEMS FROM DISTNORY
#Fot removing items there is several methods available

#To remove a specific item from a distnory we use pop() methode
dict10 ={
    "key": "value",
    "name": "eswar",
    "age": 21,
    "pin": 413,
    "married": False
}
dict10.pop("key")
print(dict10)

#To remove last item in the distnory we use popitem()
dict11 = {
    "key": "value",
    "name": "eswar",
    "age": 21,
    "pin": 413,
    "married": False
}
dict11.popitem()
print(dict11)

#To delete a perticular key:value pair we use del method
dict12 = {
    "key": "value",
    "name": "eswar",
    "age": 21,
    "pin": 413,
    "married": False
}
del dict12["age"]
print(dict12)

'''#Delete complete distonory
dict13 = {
    "key": "value",
    "name": "eswar",
    "age": 21,
    "pin": 413,
    "married": False
}
del dict13
print(dict13)#Will returns an error because it is deleted so i doesnt printed'''

#Clear everything in distonory
dict14 = {
    "key": "value",
    "name": "eswar",
    "age": 21,
    "pin": 413,
    "married": False
}
dict14.clear()
print(dict14)#will prints an empty distonory {}

#LOOPS THROUGH DISTONORY

#To print only keys in distonory
dict15 = {
    "key": "value",
    "name": "eswar",
    "age": 21,
    "pin": 413,
    "married": False
}
for x in dict15 :
    print(x)

#we can print keys by another methode also
dict16 = {
    "key": "value",
    "name": "eswar",
    "age": 21,
    "pin": 413,
    "married": False
}
for x in dict16.keys():
    print(x)

#We can print only values
dict17 = {
    "key": "value",
    "name": "eswar",
    "age": 21,
    "pin": 413,
    "married": False
}
for x in dict17:
    print(dict17[x])

#Another way to get only values
dict18 = {
    "key": "value",
    "name": "eswar",
    "age": 21,
    "pin": 413,
    "married": False
}
for x in dict18.values():
    print(x)

#To print both key:values using loop 
dict19 = {
    "key": "value",
    "name": "eswar",
    "age": 21,
    "pin": 413,
    "married": False
}
for x,y in dict19.items():
    print(x,y)

#copying a distonary in to another variable
dict20 = {
    "key": "value",
    "name": "eswar",
    "age": 21,
    "pin": 413,
    "married": False,
    "copy" : 1
}
copied = dict20.copy()
print(copied)

#another way to make a copy by using dict()
dict21 = {
    "key": "value",
    "name": "eswar",
    "age": 21,
    "pin": 413,
    "married": False,
    "copy" : 2
}
copied2 = dict(dict21)
print(copied2)

#NESTED DISTONORIES
#we can create a nested distonory superated by comma,
dict_family1 = {
    "eswar1" : {
    "name" : "eswar",
    "age" : 21,
    "married" : "NO" 
    },
    "eswar2"  : {
    "education" : "Btech",
    "branch" : "Ece",
    "pin" : 413
    },
    "eswar3" : {
    "compeny" : "Oculotronics",
    "Job" : "Enbedded",
    "salary" : 20000,
    "dict_family":1
    }
}
print(dict_family1)

#We can group all distonories, later if we want
eswar1 = {
    "name" : "eswar",
    "age" : 21,
    "married" : "NO"
}
eswar2 = {
    "education" : "Btech",
    "branch" : "Ece",
    "pin" : 413
}
eswar3 = {
  "compeny" : "Oculotronics",
    "Job" : "Enbedded",
    "salary" : 20000,
    "dict_family" : 2
}
dict_family2 = {
    "eswar1" : eswar1,
    "eswar2" : eswar2,
    "eswar3" : eswar3
}
print(dict_family2)

