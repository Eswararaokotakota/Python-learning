import math

#To get min and max values from a bunch of numbers
a = min(12,33,445,45,56,78,89,5,345,34534,345,345,345,54,3,34,5,5,1)
b = max(12,123,34,234,234,234,23,4,356,567,678,6,8,6,5,4,3,3)
print(a,"\n",b)


#To return only possitive value even if it is a -ve value then use abs()
x = abs(-53345.663)
print(x)

#For doing power of math we can use pow() function  2^3 like that
y = pow(2,5) #Two to the power of 5
print(y)
'''All the above functions are built in functions of python, they dosent need math moduleimported'''


'''Below functions need to import the math module import math'''
#SQUARE ROOT
#To do squareroot of something you can use math module
a = math.sqrt(4)
print(a)

#For getting intergervalue if there is float (round figuring) we have functions
#To set the value to the upwards nearest value
x = math.ceil(1.8)
#For downwords to the integer
y = math.floor(1.8)

#we also can mension the pi in the code by using "math.pi"
x = math.pi
print(x)#will returns the pi value 3.14...
'''Some randomecode to multiply number with pi'''
a = int(input("enter number todo pi():"))
output = a*x
print(output)


'''wehave someny math module things, learn them when its required'''