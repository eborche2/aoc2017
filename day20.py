def findshortestdistance(pos):
    man = []
    for z, each in enumerate(pos):
        if each:
            man.append(abs(each[0]) + abs(each[1]) + abs(each[2]))
    smallest = min(int(x) for x in man)
    largest = max(int(x) for x in man)
    return (smallest, man.index(smallest), largest)
with open('file20.in') as f:
    content = f.readlines()
content = [x.strip() for x in content]
pos = {}
vel = []
accel = []
for z, each in enumerate(content):
    position = each[each.index('<') + 1: each.index('>')]
    to_eval = 'pos[\'%s\'] = ((%s))' % (z, position)
    exec(to_eval)
    temp = each[each.index('>') + 1:]
    velocity = temp[temp.index('<') + 1: temp.index('>')]
    to_eval = 'vel.append((%s))' % (velocity)
    exec(to_eval)
    temp = temp[temp.index('>') + 1:]
    acceleration = temp[temp.index('<') + 1: temp.index('>')]
    to_eval = 'accel.append((%s))' % (acceleration)
    exec(to_eval)

print findshortestdistance(accel) # Part1 I'm an idiot acceleration is 0....

for u in range(1, 10000):
    for each in pos:
        pos[each] = (pos[each][0] + vel[int(each)][0] + (accel[int(each)][0] * u),
                    pos[each][1] + vel[int(each)][1] + (accel[int(each)][1] * u),
                    pos[each][2] + vel[int(each)][2] + (accel[int(each)][2] * u))
    new_pos = {}
    to_remove = []
    for each in pos:
        if pos[each] not in new_pos.values():
            new_pos[each] = pos[each]
        else:
            to_remove.append(pos[each])
    
    for each in to_remove:
        pos = {k: v for k, v in pos.iteritems() if v != each}
    
print(len(pos))# part2 No real check if 10,000 is enough, but nothing collided from 1000 to 10000
# so I figure it is a safe bet....
    