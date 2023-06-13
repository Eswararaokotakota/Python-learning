import csv

csvfiles = open("E:/Coding/sample_csv_files/0.0-1.0_10_03_2022_13_20_13_Laser1_L4.csv","r")
reader = csv.reader(csvfiles)
#header = next(csvfiles)

for x in reader:
    print(x)

csvfiles.close()