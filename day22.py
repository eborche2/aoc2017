def newcoord(direction, coord):
    if direction == 'n':
        coord = (coord[0], coord[1] - 1)
    elif direction == 's':
        coord = (coord[0], coord[1] + 1)
    elif direction == 'e':
        coord = (coord[0] + 1, coord[1])
    elif direction == 'w':
        coord = (coord[0] -1 , coord[1])
    return(coord)

def changedirect(direction, turn):
    if direction == 'n':
        if turn == 'l':
            direction = 'w'
        elif turn == 'v':
            direction = 's'
        else:
            direction = 'e'
    elif direction == 's':
        if turn == 'l':
            direction = 'e'
        elif turn == 'v':
            direction = 'n'
        else:
            direction = 'w'
    elif direction == 'e':
        if turn == 'l':
            direction = 'n'
        elif turn == 'v':
            direction = 'w'
        else:
            direction = 's'
    elif direction == 'w':
        if turn == 'l':
            direction = 's'
        elif turn == 'v':
            direction = 'e'
        else:
            direction = 'n'
    return(direction)

with open('file22.in') as f:
    content = f.readlines()
content = [x.strip() for x in content]
map = []
# Not an infinite map, but should be enough to handle 10000 circles.  
for each in range(475):
    temp = ''
    for each in range(1000):
        temp += '.'
    map.append(temp)
for x in range(25):
    temp = ''
    for each in range(475):
        temp += '.'
    temp += content[x]
    for each in range(500):
        temp += '.'
    map.append(temp)
for x in range(500):
    temp = ''
    for each in range(1000):
        temp += '.'
    map.append(temp)
coord = (487, 487)
direction = 'n'
count = 0
for x in range(10000000):
    if map[coord[1]][coord[0]] == '#':
        direction = changedirect(direction, 'r')
        map[coord[1]] = map[coord[1]][:coord[0]] + 'f' + map[coord[1]][coord[0]+1:]
    elif map[coord[1]][coord[0]] == 'w':
        map[coord[1]] = map[coord[1]][:coord[0]] + '#' + map[coord[1]][coord[0]+1:]
        count += 1
    elif map[coord[1]][coord[0]] == 'f':
        direction = changedirect(direction, 'v')
        map[coord[1]] = map[coord[1]][:coord[0]] + '.' + map[coord[1]][coord[0]+1:]
    else:
        direction = changedirect(direction, 'l')
        map[coord[1]] = map[coord[1]][:coord[0]] + 'w' + map[coord[1]][coord[0]+1:]
        
    coord = newcoord(direction, coord)

z = 1
for x in range(475, 500):
    print(z, map[x][475:500])
    z += 1

print(count) #Part 1 and Part 2 Modified You could comment out the two middle elifs and put count in the second else for part 1.
    
    
        
