# assignment print colors in uppercase once using a loop
colors = ['red','blue','green','yellow']
i = 0
while i < len(colors):
    for color in colors:
        print(color.upper())
    i = i+1

# lists (task is to combine them into one, 'fav food' dictionary)
maryFavFood = ['beef','chicken','vegetable']
janeFavFood = ['rice','ugali','mahindi choma']
favFood = {
    'mary':['beef','chicken','vegetable'],
    'jane':['rice','ugali','mahindi choma']
    }
print(favFood)

# mary with email and password same with jane