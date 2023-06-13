
# for x in "banana":
#     print(x)

# text ="iam an embedded engineer"
# print("embedded" in text)

# text1 ="i am learning python now"
# if "learning" in text1:
#     print("yes i know you are learning python")

# text2 = "now learning about string operations in python"
# print("python" not in text2)

# text3 = "this is awesome that i can do meny operations in python"
# if "bomb" not in text3:
#     print("man! bomb not in python")
#     print("check once",text3)


data2 = ["tanooj","kumar","sudhabathula","booom"]
for x in data2:
    if x == "tanooj":
        data2.remove("tanooj")
        data2.append("eswar")
print(data2)