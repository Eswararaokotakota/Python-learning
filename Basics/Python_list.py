#The list is a colection  which is orderd and changable and also allows duplicate members
#python lists are written in square brackets[]

#creating a list



the_list=["eswar","rao","kottakota","btech","ece"]
print(the_list)

#get one value from list
list =["mango","banana","apple","pinapple","strawberry"]
print(list[2])

#getting multiple values from list
list =["mango","banana","apple","pinapple","strawberry"]
print(list[2:4])

#to change the specific item, reffer the index number
list =["mango","banana","apple","pinapple","strawbbrry"]
list[1] = "laddu"
print(list) 


#to kmow how meny items exists in the list
list =["mango","banana","apple","pinapple","strawberry"]
print(len(list))

#To add another item in to the list we use append methode
list =["mango","banana","apple","pinapple","strawberry"]
list.append("kiwi")
print(list)
print("append above")

#To add an item in a perticular index location we use insert
list =['mango', 'banana', 'apple', 'pinapple', 'strawberry', 'kiwi']
list.insert(3,"dragon fruit")
print(list)

#to remove a specified item we use remove methode
list =['mango', 'banana', 'apple', 'dragon fruit', 'pinapple', 'strawberry', 'kiwi']
list.remove("dragon fruit")
print(list)

#to remove item based on the specific index number we use pop method
list =['mango', 'banana', 'apple', 'dragon fruit', 'pinapple', 'strawberry', 'kiwi']
list.pop(1)
print(list)
#If the item index number is not specified then the last item inthe index will be removed
list = ['mango', 'banana', 'apple', 'dragon fruit', 'pinapple', 'strawberry', 'kiwi']
list.pop()
print(list)

#To clear everything in the list we use clear() methode
list =['mango', 'banana', 'apple', 'dragon fruit', 'pinapple', 'strawberry', 'kiwi']
list.clear()
print(list)

#To print the list items reverse order we use reverse
list = ["ball","bat","stemper","mrf","wickets","score","six","bat","four","bat","empaire","ground"]
list.reverse()
print(list)

#loop through the list
list =["mango","banana","apple","pinapple","strawberry"]
for x in list :
    print(x)

#check if the item exist in the list
list =["mango","banana","apple","pinapple","strawberry"]
if "apple" in list:
    print("yes, apple exists in the list")


#total methods that we can use for list are:
#  len() append() insert() remove() pop() clear()

#sort methode in list

#The sort will arange the list items alphabetically
llist =['mango','banana','apple','pinapple','strawberry']
llist.sort()
print(llist)

#list to print it revers alphabet order
list =['mango','banana','apple','pinapple','strawberry']
list.sort(reverse=True)
print(list)

#to get the position of an item in the list we use index it starts from 0
list1=["ball","bat","stemper","mrf","wickets","score","empaire","ground"]
print(list1.index("bat"))
#or you can just assign a variable for the index number and then call it later
list=["ball","bat","stemper","mrf","wickets","score","empaire","six","ground"]
x = list.index("ground")
print(x)

#To know how meny times a item repeated in the list we use count 
list1=["ball","bat","stemper","mrf","wickets","score","six","bat","four","bat","empaire","ground"]
print(list1.count("bat"))
#again you can assign a variable for this
list1=["ball","bat","stemper","mrf","wickets","score","six","bat","four","bat","empaire","ground"]
x = list1.count("bat")
print(x)

#To add another list elements to the existed list we use extend 
list1 = ["ball","bat","stemper","mrf","wickets","score","six","bat","four","bat","empaire","ground"]
list =["dhoni","virat","sachin","gail"]
list1.extend(list)
print(list1)

#To copy the list items we use copy() methode
list = ["ball","bat","stemper","mrf","wickets","score","six","bat","four","bat","empaire","ground"]
x = list.copy()
print(x)


#Performing sort operations with functions, it will shorts the list 
#denepding the no letters containingin it
def my_fuction(e):
    return len(e)
list=["sort","len","clear","extend","pop","copy","bo"]
list.sort(key=my_fuction)
print(list)

#it will print reverse order for the above from highest no of charecters to less no of characters
def my_function2(e):
    return len(e)
list=["sort","len","clear","extend","pop","copy","bo"]
list.sort(reverse=True, key=my_function2)
print(list)

#now we are playing with the distonory
#here it will prints the things based on the year number from low to high
def my_function3(e):
    return e['year']
car=[
    {'car':'skoda','year':2020},
    {'car':'audi','year':2025},
    {'car':'benz','year':1998},
    {'car':'kia','year':2023},
    {'car':'tesla','year':2039}
]
car.sort(key=my_function3)
print(car)


list_sum = [1,2,3,4,5,6,7,8,9,0,123,12,214]
print(sum(list_sum))
'''Final over view
we learned the different types operations that can be used to 
do with list in python
      Those are
      #total methods that we can use for list are:
1.len()
2.append()
3.insert()
4.remove()
5.reverse()
6.pop()
7.clear()
8.extend()
9.del()
10.sort()
11.sort(reverse=True)
12.copy()
13.count()
14.index()  
'''