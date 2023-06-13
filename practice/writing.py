import csv

Headers = ["Age","Branch","Date_of_Joining","Mobile_Number"]
data = [21,"ECE",2022,6301189779]
data1 = [21,"ece",2022,8639551503]
data2 = [22,"ece",2023,7702357500]

filu = open("E:/Coding/Python/practice/writing.csv","w")

write = csv.writer(filu)

write.writerow(Headers)

write.writerow(data)

write.writerow(data1)

write.writerow(data2)

filu.close()