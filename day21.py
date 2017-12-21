def check_match(block, match, grid):
    for j, each in enumerate(match):
        if len(each) == len(block):
            for z in range(4):
                temp = block
                if each == block:
                    return j
                else:
                    if grid == 3:
                        block = block[6:7] + block[3:4] + block[0:1] + block[7:8] + block[4:5] + block[1:2] + block[8:9] + block[5:6] + block[2:3]
                    else:
                        block = block[2:3] + block[0:1] + block[3:4] + block[1:2]
                temp = block
                if grid == 3:
                    block = block[2:3] + block[1:2] + block[0:1] + block[5:6] + block[4:5] + block[3:4] + block[8:9] + block[7:8] + block[6:7]
                else:

                    block = block[1:2] + block[0:1] + block[3:4] + block[2:3]
                if each == block:
                        return j
                block = temp
                if grid == 3:
                    block = block[6:7] + block[7:8] + block[8:9] + block[3:4] + block[4:3] + block[5:6] + block[0:1] + block[1:2] + block[2:3]
                else:
                    block = block[2:3] + block[3:4] + block[0:1] + block[1:2]
                if each == block:
                        return j
                block = temp
def figure_rule(start, side, match, convert):
    grid = len(start[0]) / side
    blocks = []
    x = 0
    y = 0
    for row in range(side):
        for col in range(side):
            if grid == 2:
                blocks.append(start[y][x:x+2] + start[y+1][x:x+2])
                x += 2
            else: 
                blocks.append(start[y][x:x+3] + start[y+1][x:x+3] + start[y+2][x:x+3])
                x += 3
        if grid == 2:
            y += 2
            x = 0
        else:
            y += 3
            x = 0
    matched = []
    for each in blocks:
        matched.append(check_match(each, match, grid))
    return(matched)

with open('file21.in') as f:
    content = f.readlines()
content = [x.strip() for x in content]
match = []
convert = []
for each in content:
    temp = each[:each.index('/')]
    place = each[each.index('/') + 1:]
    if place.index('/') > place.index('='):
        match.append(temp + place[:place.index(' ')])
    else:
        match.append(temp + place[:3] + place[4:7])
    place = place[place.index('>') + 2:]
    temp = []
    if place.count('/') == 3:
        temp.append(place[:4])
        temp.append(place[5:9])
        temp.append(place[10:14])
        temp.append(place[15:])
    else:
        temp.append(place[:3])
        temp.append(place[4:7])
        temp.append(place[8:])
    convert.append(temp)
start = ['.#.', '..#', '###']
for z in range(18):
    new_start = []
    if len(start[0]) % 2 == 0:
        side = (len(start[0]) / 2)
        factor = side ** 2
        block = figure_rule(start, side, match, convert)
    else:
        side = (len(start[0]) / 3)
        factor = side ** 2
        block = figure_rule(start, side, match, convert)
    blocks = []
    for each in block:
        blocks.append(convert[each])
    each_side = int(len(blocks)**(1/2.0))
    for x in range(each_side):
        for y in range(len(blocks[0][0])):
            row = ''
            for j in range(x * side, x*side + side):
                row += blocks[j][y]
                
            new_start.append(row)     
    start = new_start
 
    if z == 4:
        count = 0
        for each in start:
            count += each.count('#')
        print(count) # part 1
        
count = 0
for each in start:
    count += each.count('#')
print(count) # part 2