with open('file11.in') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
directions = content[0].split(',')
coordinates = []
coordinates.append({'x': 0, 'y': 0})
for each in directions:
    x = 0
    if 'e' in each:
        x = 1
    elif 'w' in each: 
        x = -1
    if x == 0:
        if 'n' in each: 
            y = 2
        else:
            y = -2
    else:
        if 'n' in each:
            y = 1
        elif 's' in each: 
            y = -1
    last = coordinates[-1:]
    x = last[0]['x'] + x
    y = last[0]['y'] + y
    coordinates.append({'x' :x, 'y': y})
last = coordinates[-1:][0]
x = last['x']
y = last['y']


def test(x, y):
    not_home = True
    steps = 0
    while not_home:
        if x == 0 and y == 0:
            not_home = False
            print(steps)# part 1
        elif x == 0:
            if y == 1:
                y += 1
                x ++ 1
            elif y == -1:
                y -= 1
                x -= 1
            if y > 0:
                y -= 2
            else:
                y += 2
            steps += 1
        else:
            if x > 0:
                x -= 1
            else:
                x += 1
            if y > 0:
                y -= 1
            else: 
                y += 1
            steps += 1
test(x, y) #part 1
x = 0
x2 = 0
y = 0
y2 = 0
for each in coordinates:
    if abs(each['x']) > abs(x):
        x = each['x']
        y = each['y']
    if abs(each['y']) > abs(y2):
        x2 = each['x']
        y2 = each['y']
test(x, y) #banking that either the greatest x or greatest y will be the 
test(x2, y2) #most steps. 
        
    

