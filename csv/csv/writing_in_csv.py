import csv

Headers = ["Age","Branch","Date_of_Joining","Mobile_Number"]
data = [21,"ECE",2022,6301189779]

eswar = open("E:/Coding/Python/tasks/csv/generated_csv_files/employe.csv","w")

writer = csv.writer(eswar)

writer.writerow(Headers)

writer.writerow(data)

eswar.close()
print("------------------------Done Writing!-------------------------")