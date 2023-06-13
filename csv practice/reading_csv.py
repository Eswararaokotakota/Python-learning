import csv

file1 = open("C:/Users/Eswar/Desktop/csv practice/address.csv")

reader = csv.reader(file1)

# header = next(reader)
# print(header)

row=[]

for rows in reader:
    row.append(rows)
print(row)

file1.close() 