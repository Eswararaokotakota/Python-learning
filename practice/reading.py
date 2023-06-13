import csv
from hashlib import new

files = open("E:/Coding/Python/practice/reading.csv","r")
reader = csv.reader(files)

header = next(reader)
print(header)

rows=[]

for row in reader:
    rows.append(row)

print(rows)

files.close()


#Then writing
data1 = ["eswar","rao","kottakota","boom","bomb"]
data2 = ["tanooj","kumar","sudhabathula","booom"]
data3 = ["tan","ku","sudha","booooooooom"]

files1 = open ("E:/Coding/Python/practice/reading.csv","a",newline="")#newline="" will avoid printing the new empty line

writer = csv.writer(files1)

writer.writerow(data1)
writer.writerow(data2)
writer.writerow(data3)

files1.close()