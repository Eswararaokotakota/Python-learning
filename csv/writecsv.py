import csv

head = ["name","age","study","pin"]#data will be written in csv file from this lists
data = ["eswar",21,"B.tech",413]
data1 = ["rao",22,"Mtech",413]

file = open("E:/Coding/Python/csv/data2.csv","w")#if csv file* already exists it will write in it
                                                 #if csv file doesnt exists then it will creates a csv file and then writes the data in it

writer = csv.writer(file)#making a writer object to write in csv file

writer.writerow(head)#it will writes the data exist in the head list

writer.writerow(data)#Then it will writes another row in the next line from data list

writer.writerow(data1)

file.close()#We should close the csv file after opening
print("------------------Done writing------------------")