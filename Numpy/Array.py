import numpy as np
# 0D Array
array = np.array([2])
print (array)

# 1D array
array1=np.array([1,2,3,4,5])
print(array1)

# 2D array
array2 = ([(1,2,3,4),(6,7,8,9,0)])
print(array2)
print(array2[1])#printes the index[1] array (6,7,8,9,0)


#Note
#the type of array object is an ND ARRAy  
print(type(array1)) #says its an ndarray(d = dimentional)

# We can create numpy arrays with specified values like 0 ,1 
zeros_array = np.zeros(3, np.int32) #without int32 it will print a pulstop after each zero
print(zeros_array)

# We can also create multidimentional arrays with our specified valuezero
zero_arrays = np.zeros((3,6), np.int32) #3 rows 6 columns
print(zero_arrays)

# wee can also print ones as we print zeros before
one_array = np.ones((6,9), np.int32)
print(one_array)

#we can create zeros and ones as a array shape that already we have 
shape_copy = np.zeros_like(array2)
print(shape_copy)

shape_copy1 =np.ones_like(array2)
print(shape_copy1)
    
# We can print the randome numbers between the given range by using randome function
randome = np.random.randint(1,1000,30) 
print(randome)  #will prints 30 randome numbers from 1 to 1000

#We can also ask to print randome numbers in 2 dimentional
randome1 = np.random.randint(1,1000,(4,7)) #4 rows 7columns with randome numbers
print(randome1)


#we can also reshape the array without changingthe data in it
reshaping = randome1.reshape((7,4))
print(reshaping) #will reshapes the array from 4r & 7c  to  7r & 4c

