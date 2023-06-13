# import csv
# data = ["b181",22,17,40,214,39,"*","7E"]
# file = open("C:\\Users\\Eswar\\Desktop\\gpsdata.csv","w")
# writer = csv.writer(file)

# writer.writerow(data)

# file.close()
import numpy as np
import random
Branch_data = ["ECE","CSE","EEE","CIVIL","MECH"]

    
data1 = []

for data in range(0,1000):
    mobile = random.getrandbits(32)
    age_data = random.randrange(18,100)
    Branch = random.choice(Branch_data)
    day_data = random.randrange(1,31) 
    month_data = random.randrange(1,12)
    year_data = random.randrange(2021, 2025)
    data1.append(str(age_data))
    data1.append(str(mobile))
    data1.append(str(Branch))
    a = (day_data,"-",month_data,"-",year_data)
    data1.append(a)
    b = len(data1)
    c = np.array(data1)
    e = c.reshape(b,1)
    print(e)