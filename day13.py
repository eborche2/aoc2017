with open('file13.in') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
firewall = {}
size = 0
for i, each in enumerate(content):
    firewall[each[:each.index(':')]] = int(each[each.index(' ')+1:])
    if i == len(content) -1:
        size = int(each[:each.index(':')]) + 1
caught = ['0']
for x in range(1, size):
    if str(x) in firewall:
        depth = firewall[str(x)]
        if x % ((depth * 2 -2)) == 0:
            caught.append(str(x))
total = 0
for key in caught:
    total += int(key) * firewall[key]
print(total) #part 1
seconds = 0
while len(caught) > 0:
    seconds += 1
    del caught[:]
    for x in range(size):
        if str(x) in firewall:
            depth = firewall[str(x)]
            
            if (x + seconds) % ((depth * 2 - 2)) == 0:
                caught.append(str(x))
                break
    if seconds % 100000 == 0:
        print(seconds)
print(seconds)