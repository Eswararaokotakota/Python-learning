#Tuple is collection which is ordered and unchangable

tuple = ("laptop","battery","screen","ram","graphic card","cpu","south bridge")
print(tuple)

#Accessing the touple item based on index value
tuple1 = ("laptop","battery","screen","ram","graphic card","cpu","south bridge")
print(tuple1[4])


#To know the length of tuple we use len() same as list
tuple3 = ("laptop","battery","screen","ram","graphic card","cpu","south bridge")
print(len(tuple3))

#we can construct a tuple with tuple()
# tuple4 = tuple(("mobile","battery","touch screen","rare camera","front camera"))
# print(tuple4)

#loop through tuple
tuple5 = ("mobile","battery","touch screen","rare camera","front camera")
for x in tuple5:
    print(x)

tuple6 = ("mobile","battery","touch screen","rare camera","front camera")
if "batery" in tuple6:
    print("yes, battery exist in tuple")

#We canot change the value of tuple
tuple7 = ("laptop","battery","screen","ram","graphic card","cpu","south bridge")
tuple[4]="bomb"
print(tuple7)
#It will remain same because we cannot change the tuple items or values

#We cant remove the items in th tuple but we can delete the tuple completely
tuple8 = ("laptop","battery","screen","ram","graphic card","cpu","south bridge")
del tuple8
print(tuple8)
#it will gives you an error because it will be deleted completely  error: (NameError: name 'tuple4' is not defined)

#if condition in tuple
tuple9 = ("tanooj","neehar anna","eswar","neveen anna","ramarao")
if "ramarao" in tuple9:
    print("ramarao exist")

#loop in tuple 
tuple10 = ("Road runner","bulero","lcms","laser","camera","i/o control panel")
for x in tuple10:
    print(x)