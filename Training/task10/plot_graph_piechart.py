import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("E:\\Coding\\Python\\Training\\task_1\\employe_data.csv")

def bargraph():
    df = pd.DataFrame(data)

    x = list(df.iloc[:,1])
    y = list(df.iloc[:,0])
    plt.bar(x, y, color="red")
    plt.show()

def piechart():
    age_data = data["Age"]
    branch_data= data["Branch"]
    colors = ["red","white","blue","skyblue"]
    plt.pie(age_data, labels=branch_data, colors=colors)
    plt.show()

piechart()