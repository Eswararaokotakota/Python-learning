import datetime

x = datetime.datetime.now()
print(x)#will prints the exat date and time of the exucution instant

#we can get specific date or year or month or hour by mensioninng themsuperately
print(x.year) #will prints the month
print(x.month) #will prints month number
print(x.strftime("%A"))#will prints the day name

#we can create a date object 
y = datetime.datetime(2000,10,10) 
print(y) #Will prints date as given and remaining time to zero / you can assign the time also it will prints it
#here it is
z = datetime.datetime(2000,10,10,12,30,12)
print(z)

#we can change the date times to readable strings using strftime() finction
x = datetime.datetime(2001,10,13)
print(x.strftime("%B")) #will prints the month name

print(x.strftime("%a")) #day  mon,tues,etc.. 
print(x.strftime("%A")) #shortcuts of day will prints full name if u use "%A" capital A

#and someny directives(ex."%a") are available search and learn when required



