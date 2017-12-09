def remove_exc(content):
    to_remove = []
    skip = False
    for x, each in enumerate(content):
        if each == '!':
            if skip:
                skip = False
            else:
                to_remove.append(x)
                to_remove.append(x+1)
                skip = True
        else:
            if skip:
                skip = False
    to_remove.sort(reverse=True)
    for each in to_remove:
        content = content[:each] + content[each+1:  ]
    return content
def remove_garbage(content):
    to_remove = []
    compare = '<'
    for x, each in enumerate(content):
        if each == compare:
            to_remove.append(x)
            if compare == '<':
                compare = '>'
            else:
                compare = '<'
    to_remove.sort(reverse=True)
    skip = False
    removed = []
    for z, each in enumerate(to_remove):
        if skip:
            skip = False
        else:
            content = content[:to_remove[z+1]] + content[each+1:]
            removed.append((each) - (to_remove[z+1]) - 1)
            skip = True
    total = 0
    for each in removed:
        total += each
    print(total)# part 2
    return content
            
with open('file9.in') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = content[0]
content = remove_exc(content)
content = remove_garbage(content)
counts = []
scale = 0
for each in content:
    if each == '{':
        scale += 1
        counts.append(scale)
    elif each == '}':
        scale -= 1
total = 0
for each in counts:
    total += each
print(total) # part 1

    