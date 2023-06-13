#Set
#Sets are un-ordered and un-indexed
set ={"camera","battery","50mm","200mm",1.8,413}
print(set)

#loop through the set
set1 ={"camera","battery","50mm","200mm",1.8,413}
for x in set1:
    print(x)

#check if the value or item exist in the set
set2 ={"camera","battery","50mm","200mm",1.8,413}
if 1.8 in set2:
    print("yes 1.8 exist in the set you have")

#Adding items in the set add()
set3 ={"camera","battery","50mm","200mm",1.8,413}
set3.add("lens")
print(set3)

#To add multiple items in a set we use update()
set4 ={"camera","battery","50mm","200mm",1.8,413}
set4.update(["lens","gimbal","sungun","reflector"])
print(set4)

#To remove last item in the set we use pop()
set5 ={"camera","battery","50mm","200mm",1.8,413}
x = set5.pop()
print(x)
print(set5)
#it will randomly removes one item and prints remaining items in it

#To remove a item in the set we can use  remove() or the discard() methods
set6 ={"camera","battery","50mm","200mm",1.8,413}
set6.remove("camera")
set6.discard("50mm")
print(set6)

#To clear a set we use clear()
set7 ={"camera","battery","50mm","200mm",1.8,413}
set7.clear()
print(set7) 
print("//clear()")

# #To completely delete a set we use del()
# set8 ={"camera","battery","50mm","200mm",1.8,413}
# del set8
# print(set8)
# #It will prints an error becaues it is deleted 

#to compare two sets and to eliminate the common items and prints the remaining in the sets we use differance()
set9 = {"camera","battery","50mm","200mm",1.8,413,"lens","sony","canon","differance"}
set10 = {"laptop","mobile","tab","keypad","nokia","camera","battery"}
x = set9.difference(set10)
print(x)

#We can sonstruct a set by  set(())
# set11 = set(("camera","battery","50mm","200mm",1.8,413,"lens","sony","canon"))
# print(set11)

#it will prints the items expect the common items
# set12 = {"camera","battery","50mm","200mm",1.8,413,"lens","sony","canon","differance"}
# set13 = {"laptop","mobile","tab","keypad","nokia","camera","battery","200mm"}
# y = set12.symmetric_difference(set13)
# print(y)


# #Remove the items that are present in both sets, AND insert the items that is not present in both sets:
# set14 = {"camera","battery","50mm","200mm",1.8,413,"lens","sony","canon","differance"}
# set15 = {"laptop","mobile","tab","keypad","nokia","camera","battery","200mm"}
# z = set14.symmetric_difference_update(set14)
# print(z)

#Return a set that contains the items that exist in both set x, and set y:
set16 = {"banana","apple","grape","pinapple"}
set17 = {"kiwi","sweet"}
a = set16.intersection(set17)
print(a)