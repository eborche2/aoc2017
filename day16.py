with open('file16.in') as f:
    content = f.readlines()

content = [x.strip() for x in content]
content = content[0].split(',')
dance = "abcdefghijklmnop"
def flipdance(first, second, dance):
    if first < second:
        temp = first
        first = second
        second = temp
    return dance[:second] +  dance[first] + dance[second+1:first] + dance[second] + dance[first+1:]
dancelist = []
found = False
count = 0
while found == False:
    for each in content:
        if 's' == each[:1]:
            flip = 16 - int(each[1:])
            dance = dance[flip:] + dance[:flip]
        elif 'x' == each[:1]:
            temp = each[1:]
            tempfirst = int(temp[:temp.index('/')])
            tempsecond = int(temp[temp.index('/')+1:])
            dance = flipdance(tempfirst, tempsecond, dance)
        elif 'p' == each[:1]:
            temp = each[1:]
            firstflip = temp[:temp.index('/')]
            secondflip = temp[temp.index('/')+1:]
            dance = flipdance(dance.index(firstflip), dance.index(secondflip), dance)
    if dance in dancelist:
        found = True
    else:
        dancelist.append(dance)
        count += 1

    
print(dancelist[0]) #part 1
value = 0
if 1000000 % count  == 0:
    value = count -1
else:
    value = (1000000 % count) - 1
print(dancelist[value]) #part 2

    

        
