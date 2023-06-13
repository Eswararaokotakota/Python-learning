import csv

head = ["name","graduation","job","job role","package"]

data1 = ["Eswar","B-Tech","yes","embedded engineer",240000]

myfile = open("address.csv","w")

writer = csv.writer(myfile)

writer.writerow(head)

writer.writerow(data1)

myfile.close()