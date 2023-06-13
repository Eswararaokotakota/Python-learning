import csv



file = open ("E:\\Coding\\Python\\csv\\csv\\dict.csv","w",newline="")
header = ["name","age","branch"]

dict = [
    {'name':"eswar",'age':21,'branch': "ECE"},
    {'name':"rao",'age':22,'branch': "EEE"},
    {'name':"boom",'age':23,'branch': "mech"}]


with open("dict.csv","w",newline="") as csv_file:
    writer = csv.DictWriter(file,feildnames=header)

    writer.writeheader()

    for data in dict:
        writer.writerow(data)

file.close()