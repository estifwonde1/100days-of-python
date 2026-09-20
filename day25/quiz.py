import pandas as pd

data= pd.read_csv("squirrel_data.csv")
# data_list = data.to_dict()
data_fur = data["Highlight Fur Color"].to_list()
# Gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
# Cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
# print(Gray_squirrel)
# print(Cinnamon_squirrel)
Colors = ["Gray","Cinnamon","Black","White","Red"]
get = data[data["Primary Fur Color"] == "Gray"]
print(get.X.to_list())
def Color_Count(color):
    colors= len(data[data["Primary Fur Color"] == color])
    print(colors)
for color in Colors:
    Color_Count(color)
# cinnamon =[]
# grey = []
# red = []
# others=[]
# for dat in data_fur:
#     if dat == "Cinnamon":
#         cinnamon.append(dat)
#     elif dat == "Gray":
#         grey.append(dat)
#     elif dat == "Red":
#         red.append(dat)
#     else:
#         others.append(dat)
# data_dict = {
#     "Color" : ["Cinnamon", "Grey", "Red", "Others"],
#     "Count" : [len(cinnamon),len(grey),len(red),len(others)]


# }
# print(len(cinnamon))
# counter = pd.DataFrame(data_dict)
# counter.to_csv("color_count.csv")

# print(data_fur[4])
