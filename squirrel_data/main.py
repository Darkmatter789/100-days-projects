import pandas

data = pandas.read_csv('squirrel_data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

fur_colors = data['Primary Fur Color']
gray = fur_colors[fur_colors == 'Gray'].count()
red = fur_colors[fur_colors == "Cinnamon"].count()
black = fur_colors[fur_colors == "Black"].count()

data_dict = {
    "Fur Color": ["gray", "cinnamon", "Black"],
    "Count": [gray, red, black]
}

new_data = pandas.DataFrame(data_dict)

new_data.to_csv("squirrel_data/squirrel_counts.csv")