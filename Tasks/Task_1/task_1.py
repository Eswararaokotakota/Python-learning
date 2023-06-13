import random

file = open("E:\\Coding\\Python\\tasks\\Task_1\\employe_data.csv", "w")

file.write("Age" + "," + "Branch" + "," + "Date_of_join" + "," +"Mobile"+"\n")

data1 = []
Branch_data=["ECE","CSE","EEE","CIVIL","MECH","ROBOTICS","INSTRUMENTATION"]

for i in range(0,1000):
    age = random.randrange(18,50)
    Branch = random.choice(Branch_data)
    day = random.randrange(1,31)
    month = random.randrange(1,12)
    year = random.randrange(2022,2028)
    d_o_j = (str(day)+"/"+str(month)+"/"+str(year))
    mobile1 = random.randrange(63,99)
    mobile2 = random.getrandbits(26)
    mobile = (str(mobile1)+str(mobile2))
    file.write(str(age) +','+ Branch + ","+  str(d_o_j)+ "," + str(mobile) +"\n" )
file.close()

print("------------------done writing--------------------")