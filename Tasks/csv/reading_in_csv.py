import csv



eswar = open("E:/Coding/Python/tasks/csv/generated_csv_files/employe.csv","r")

csvreader = csv.reader(eswar)

header = next(csvreader)

print(header)

rows=[]

for row in csvreader:
     rows.append(row)
print(rows)
     
eswar.close()
