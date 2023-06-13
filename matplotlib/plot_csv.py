import pandas as pd
import matplotlib.pyplot as plt


columns =["Age"]
df = pd.read_csv("E:\\Coding\\Python\\Tasks\\Task_1\\employe_data.csv", usecols=columns)
plt.plot(df)
plt.show()

columns1 = ["Mobile"]
df1 = df = pd.read_csv("E:\\Coding\\Python\\Tasks\\Task_1\\employe_data.csv", usecols=columns1)
print(df1)
plt.plot(df1)
plt.show()