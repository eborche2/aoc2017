def determineturn(pos, mapped, direction):
    if direction == 's' or direction == 'n':
        east = ((pos[0] + 1), pos[1])
        west = ((pos[0] - 1), pos[1])
        try:
            eastinstruc = mapped[abs(east[1])][east[0]]
        except:
            eastinstruc = None
        try: 
            westinstruc = mapped[abs(west[1])][west[0]]
        except:
            westinstruc = None
        if eastinstruc:
            if eastinstruc != ' ' and eastinstruc != '|':
                direction = 'e'
        if westinstruc:
            if westinstruc != ' ' and westinstruc != '|':
                direction = 'w'
    else:
        north = (pos[0], (pos[1] + 1))
        south = (pos[0], (pos[1] - 1))
        try:
            northinstruc = mapped[abs(north[1])][north[0]]
        except:
            northinstruc = None
        try: 
            southinstruc = mapped[abs(south[1])][south[0]]
        except:
            southinstruc = None
        if northinstruc:
            if northinstruc != ' ' and northinstruc != '-':
                direction = 'n'
        if southinstruc:
            if southinstruc != ' ' and southinstruc != '-':
                direction = 's'
    return(direction)

def move(pos, direction, letter, mapped):
    end = False
    if direction == 's':
        pos = (pos[0], (pos[1] - 1))
    elif direction == 'n':
        pos = (pos[0], (pos[1] + 1))
    elif direction == 'e':
        pos = ((pos[0] + 1), pos[1])
    else: 
        pos = ((pos[0] - 1), pos[1])
    
    instruc = mapped[abs(pos[1])][pos[0]]
    if instruc == '|':
        pass
    elif instruc == '-':
        pass
    elif instruc == '+':
        direction = determineturn(pos, mapped, direction)
    elif instruc == ' ':
        end = True
    else:
        letter.append(instruc)
    return end, pos, direction, letter
    
        
with open('file19.in') as f:
    content = f.readlines()
content = [x[:len(x)-2] for x in content]

mapped = []
for each in content:
    temp = []
    for x in each:
        temp.append(x)
    mapped.append(temp[:])
    del temp[:]
for z, x in enumerate(mapped[0]):
    if x == '|':
        start_pos = (z, 0)

direction = 's'
letter = []
end = False
pos = start_pos
step = 0
while end == False:
    step += 1
    end, pos, direction, letter = move(pos, direction, letter, mapped)
print(letter)# part 1
print(step)# part 2