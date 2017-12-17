step = 354
buffer = [0]
loc = 0

def findnextloc(l, b, s, length=None):
    if length:
        if s > length:
            next_step = s % length
        else:
            next_step = s
        nextloc = l + next_step
        if nextloc > length - 1:
            nextloc = nextloc - length
        return nextloc
    else:
        if s > len(b):
            next_step = s % len(b)
        else:
            next_step = s
        nextloc = l + next_step

        if nextloc > len(b) -1:
            nextloc = nextloc - len(b)
        return nextloc
        
for x in range(1,2018):
    loc = findnextloc(loc, buffer, step)
    
    nextloc = loc + 1
    
    buffer = buffer[:nextloc] + [x] + buffer[nextloc:]
    loc = nextloc
    if x % 100000 == 0:
        print(x)
lastloc = buffer.index(2017)
if lastloc > len(buffer) -1:
    lastloc = -1
print(buffer[lastloc+1]) # Part 1

# part 2
buffer = [0]
length = 1
loc = 0
for x in range(1,50000001):
    loc = findnextloc(loc, buffer, step, length) + 1
    if loc == 1:
        buffer = buffer[:1] + [x]
    length += 1
    
print(buffer) # Part 2