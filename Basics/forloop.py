a = ["eswar","rao","413","btech"]
for x in a:
    print(x)

#we can also loop through a string
b = "eswar"
for x in b:
    print(x)

#We can stop the loop when reaches perticular object
c = ["\nbreak","eswar","laptop","python\n","lcms","3drim"]
for x in c:
    #print(x)
    if x == "lcms":
        break#wil stop loop after reaching the lcms
    print(x)

#we can escape print an object by using continue statement
d = ["continue","eswar","laptop","python","lcms","3drim"]
for x in d:
    if x == "python":
        continue
    print(x)

#RANGE
#by using range() we can loop for a number of times range
for e in range(6):
    print(e)

#we can tell the starting point of range
for f in range(2,6):
    print(f)

#we can also specify the default increment number in range
for g in range(1,6,2):#the last value will tells for how meny jumps need to print
    print(g)

#we can use else in for loop also
for x in range(3):
    print(x)
else:
    print("for loop done!, else printed")

#the else will not works if we use a break statement 
for x in range(6):
    print(x)
    if x==3:
        break
else:
    print("it will not be printed because we used the break in for loop")


#we can do nested for loop
h = ["continue","eswar","laptop","python","lcms","3drim"]
i = ["\nbreak","eswar","laptop","python\n","lcms","3drim"]
for x in h:
    for y in i:
        print(x,y)

#in some situation if you dont need operation in for loop but you need to do for loop then you can use "pass" for get free fo-rom error
for x in range(8):
    pass