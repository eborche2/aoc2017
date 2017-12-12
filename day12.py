def let_merge(c_traveled, c_found, n_traveled, n_found):
    if c_found is False:
        if n_found:
            c_found = n_found
    for each in n_traveled:
        if each not in c_traveled:
            c_traveled.append(n_traveled)
    return(c_traveled, c_found)
def find_home(current, the_map, traveled, found):
    if found:
        return current, the_map, traveled, found
    else:
        if current == 0:
            found = True
            return current, the_map, traveled, found
        else:
            traveled.append(current)
            for each in the_map[current]:
                if each not in traveled:
                    ignore, ignore, tr, fd = find_home(each, the_map, traveled, found)
                    traveled, found = let_merge(traveled, found, tr, fd)
            return current, the_map, traveled, found
            
with open('file12.in') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
last = content[-1:][0]
biggest = int(last[:last.index(' ')])
value_map = [[]]*(biggest+1)
for each in content:
    array_loc = int(each[:each.index(' ')])
    to_break = each[each.index(' ')+1:]
    connected = to_break[to_break.index(' ')+1:].split(', ')
    connected = [int(x) for x in connected]
    value_map[array_loc] = connected
connected_to_home = []
not_connected_to_home = []
for x in range(biggest+1):
    traveled = []
    found = False
    ignore, ignore2, add_to_list, found = find_home(x, value_map, traveled, found)
    if found:
        for each in add_to_list:
            if each not in connected_to_home:
                connected_to_home.append(each)
    else:
        not_connected_to_home.append(add_to_list)
master_list = []
no_knew = True
while no_knew:
    no_knew = False
    master_list = []
    for each in not_connected_to_home:

        is_new = True
        for j, x in enumerate(master_list):
            if len(set(x).intersection(each)) > 0:
                is_new = False
                no_knew = True
                master_list[j] = list(set(x + each))
                break
        if is_new:
            master_list.append(each)
    not_connected_to_home = master_list[:]
print(not_connected_to_home)
print(len(connected_to_home) +1) # Part 1 Plus 1 here is the 0
print(len(not_connected_to_home) +1) # Part 2 Plus 1 here is the connected group
