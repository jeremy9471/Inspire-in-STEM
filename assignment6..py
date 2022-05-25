# assignment print colors in uppercase once using a loop
colors = ['red','blue','green','yellow']
i = 0
while i < len(colors):
    for color in colors:
        print(color.upper())
    i = i+1