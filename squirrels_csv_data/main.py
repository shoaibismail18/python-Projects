import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel=len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel=len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel=len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel)
print(red_squirrel)
print(black_squirrel)
data_dict={
    "Fur Colour" : ["Gray","Cinnamon","Black"],
    "count": [grey_squirrel,red_squirrel,black_squirrel]

}
df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
