import numpy as np

#checking thenumpy version

print(np.__version__)
#we can know the array is one dimentional or two dimentional
a = np.array([(1,2,3,4,5)])
print(a.ndim) #it will prints the 2 because we entered the above array two dimentional

print(a.itemsize)#it will gives us the size of the each element in bytes 4 bytes  (4)

print(a.dtype)#to know the datatype in the array (int32)

print(a.size)#will gives the no of el;ements in the array (6)

print(a.shape)#will gives us the shape of array



#WE CAN CONVERT ROWS TO COLUMNS
print("reshaping")
c = np.array([(1,2,3,4),(3,4,5,6)])#2 rows 4 columns
c = c.reshape(4,2) #4rows and two columns
print(c) 
print("Reshaped")


#To get perticular value from a column and row place
d = np.array([(1,3,4,5,2),(6,7,8,8,4),(9,4,3,7,33)])
print(a[0:1,3])#the 0:1 tells the array column and the next number tells the index value of the array


#To get between values from one number to another number we can di it using linespace
e = np.linspace(1,4,15)#the (1,4) is the range and the next number will tells how meny numbers i need in the range of 1,4
print(e)

#We can get the maximum and minium value of the array
f = np.array([1,4,677,3456345,745635,34,424,2,5,6])
print(f.max())#max

print(f.min())#minumum value as well

print(f.sum())#will prints the total sum of the array


#WE CAN SUM THE VALUES OF FIRST ARRAY WITH OTHER ARRAYS
g = np.array([(1,2,3,4,5),(6,4,3,5,3)])
print(g.sum(axis=0)) #wil adds the values of artray with another array based on the index value

print(g.sum(axis=1)) #will adds the values of rray one and then values of array 2 and prints the each array sum superately in a list

#we can do square root of the array
h = np.array([1,2,3,45,4])
print(np.sqrt(h)) #will gives us the aquare root of the each value in the array


#WITH TWO DIFFERENT ARRAYS
#we can add two individual arrays and prints the sum in the list format
i = np.array([(1,3,45,2),(3,5,7,8)])
j = np.array([(1,2,54,5),(45,67,67,4)])
print(i+j) #it will prints the sum of each value in the both arrays and prints them in a single array
#WE CAN ALSO PERFORM ALL ARTHMETICAL OPERATIONS SUM,MUL,SUB,DIVIDE...

#WE CAN DO STACKING OF TWO ARRAYS
print(np.vstack((i,j)))

#we can copy array by using copy function
arrcopy = h.copy()
print(arrcopy)
