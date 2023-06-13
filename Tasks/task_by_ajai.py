# a = float(input("enter a number : "))
# b = float(input("enter second number: "))
# sum = a+b
# print("the sum is : ", sum)  #done


#task to make even numbers in the list in ascending order and others as usual
#supose ifa list = [5,6,3,4,9,6,1,2] then we should move only even numbers and make it list=[5,2,3,4,9,6,1]







my_list = [9,10,5,6,7,2,8,4,8,4]
even_list=[]
index_list=[]
for i in my_list:
    if i%2==0:
        even_list.append(i)
        x = my_list.index(i)
        index_list.append(x)
         
print(even_list)
even_list.sort()

for (i,j) in zip(index_list,even_list):
    my_list[i]=j
print(my_list)