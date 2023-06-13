import random

file = open("E:\\Coding\\Python\\Training\\task_1\\employe_data.csv", "w")

file.write("Age" + "," + "Branch" + "," + "Date_of_join" + "," +"Mobile"+"\n")

Branch_data=["ECE","CSE","EEE","CIVIL","MECH","ROBOTICS","ELECTRONICS"]

for i in range(0,1000):
    age = random.randrange(18,30)
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