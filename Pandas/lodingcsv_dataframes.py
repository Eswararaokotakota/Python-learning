import pandas as pd

csvdata = pd.read_csv("E:/Coding/sample_csv_files/0.0-1.0_2022_03_10_13_20_13_Laser5_L5.csv")
final = pd.DataFrame(csvdata)
print(final)
#It will read the csv file and prints it with indexing as DataFrame output format