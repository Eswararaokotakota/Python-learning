# import random
# age = 0
# while age < 1000:
#         age_data = random.getrandbits(4)
#         age = age+1
#         print(age_data)

# print("done")

# import random
# x = 0

# while x < 1000:
#     Branch_data = ["ECE","CSE","EEE","CIVIL","MECH"]
#     # data = Branch_data.copy()
#     data =random.choice(Branch_data)
#     x += 1
#     print(data)

import random

f = open("E:\\Coding\\Python\\tasks\\Task_1\\employe_data.csv", "w")

f.write("Age" + "," + "Branch" + "," + "Date_of_join" + "," +"Mobile"+"\n")


data1 = []
Branch_data=["ECE","CSE","EEE","CIVIL","MECH"]

for i in range(0,1000):
    age = random.randrange(18,50)
    Branch = random.choice(Branch_data)
    day = random.randrange(1,31)
    month = random.randrange(1,12)
    year = random.randrange(2022,2028)
    d_o_j = (str(day)+"/"+str(month)+"/"+str(year))
    mobile = random.getrandbits(32)
    f.write(str(age) +','+ Branch + ","+  str(d_o_j)+ "," + str(mobile) +"\n" )
f.close()


print("------------------done writing--------------------")