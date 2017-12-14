def wrap(num):
    if num > 255: 
        num = num % 256
    return num
# Adding this method here rather than changing part 1 solution
def rounds(loc, step, hash_list, content):
    for each in content:
        if each <= 1:
            loc += step + each
            loc = wrap(loc)
            step += 1 
        else:
            index_end = loc + each
            wrap_middle = False
            if index_end > 255:
                wrap_middle = True
            index_end = wrap(index_end)
            if wrap_middle:
                middle = hash_list[loc:]
                middle += hash_list[:index_end]
            else: 
                middle = hash_list[loc:index_end]
            middle = list(reversed(middle))
            move_loc = loc
            for x in middle:
                hash_list[move_loc] = x
                move_loc += 1
                if move_loc > 255:
                    move_loc = 0

            loc += each + step
            loc = wrap(loc)
            step +=1
    return loc, step, hash_list
def dense(hash_list, sec):
    result = hash_list[sec+0] ^ hash_list[sec+1]
    for each in range(2, 16):
        result = result ^ hash_list[sec+each]
    return result
        
        
with open('file14.in') as f:
    content = f.readlines()

content = [x.strip() for x in content]
disk = []
for each in range(128):
    disk.append(content[0] + '-' + str(each))

full_list = []
for each in disk:
    # Everything in this for loop and the methods at the top borrowed from my hash knot solutions
    hash_list = [x for x in range(256)]
    loc = 0
    step = 0

    part_2 = [ord(x) for x in each]
    part_2 += [17,31,73,47,23]
    for x in range(64):
        loc, step, hash_list = rounds(loc, step, hash_list, part_2)
    check = hash_list [0] ^ hash_list[1]
    dense_list = []
    for each in range(16):
        dense_list.append(dense(hash_list, each*16))
    hex_answer = [hex(x)[2:] for x in dense_list]
    for i, each in enumerate(hex_answer):
        if len(each) == 1:
            hex_answer[i] = '0' + each
    answer = ''
    for each in hex_answer:
        answer += each
    full_list.append(answer)
    
bits_figured = []
for each in full_list:
    this_row = ''
    for x in each:
        this_row += str('{0:08b}'.format(int(x, 16))[4:])
    bits_figured.append(this_row)
tally = 0
for each in bits_figured:
    tally += each.count('1')
print(tally) # part 1
coordinates = []
regions = 0
def tracepaths(x, y, coordinates, bits_figured, regions):
    coordinates.append((x,y))
    if x < 127:
        if bits_figured[y][x+1] == '1':
            if (x+1, y) not in coordinates:
                tracepaths(x+1, y, coordinates, bits_figured, regions)
    if x > 0:
        if bits_figured[y][x-1] == '1':
            if (x-1, y) not in coordinates:
                tracepaths(x-1, y, coordinates, bits_figured, regions)
    if y < 127:
        if bits_figured[y+1][x] == '1':
            if (x, y+1) not in coordinates:
                tracepaths(x, y+1, coordinates, bits_figured, regions)
    if y > 0:
        if bits_figured[y-1][x] == '1':
            if (x, y-1) not in coordinates:
                tracepaths(x, y-1, coordinates, bits_figured, regions)
    regions = regions + 1
    return regions
            

for y, each in enumerate(bits_figured):
    for x, curr in enumerate(each):
        if curr == '1':
            if (x, y) not in coordinates:
                regions = tracepaths(x, y, coordinates, bits_figured, regions)
print(regions) # part 2
                
        