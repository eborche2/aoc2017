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
        
        
with open('file10.in') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
part_2 = content

content = [int(x) for x in content[0].split(",")]
hash_list = [x for x in range(256)]
loc = 0
step = 0

# part 2 solution between here and part 1
part_2 = [ord(x) for x in part_2[0]]
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
print(answer) #part 2
        
# part 1 is down here   

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
 
print(hash_list[0] * hash_list[1])# part 1 
        
        