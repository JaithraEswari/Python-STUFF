import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_count = data["Primary Fur Color"].value_counts()['Gray']
cinnamon_count = data["Primary Fur Color"].value_counts()['Cinnamon']
black_count = data["Primary Fur Color"].value_counts()['Black']

sdata = {"Fur Color": ["grey", "cinnamon", "black"], "Count": [gray_count, cinnamon_count, black_count]}

new_data = pandas.DataFrame(sdata)
new_data.to_csv("new_data.csv")