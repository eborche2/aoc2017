with open('file18.in') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

regs = {}
instrucs = []
x = []
y = []
asc = 97
for z in range(16):
    regs[str(unichr(asc))] = 0  
    asc += 1
for i, each in enumerate(content):
    instrucs.append(each[:each.index(' ')])
    temp = each[each.index(' ') + 1:]

    if instrucs[i] == 'rcv' or instrucs[i] == 'snd':
        x.append(temp)
        y.append(0)
    else:
        x.append(temp[:temp.index(' ')])
        y.append(temp[temp.index(' ') + 1:])
done = False
loc = 0
last_sent = None

while done == False:
    
    try: 
        ytry = int(y[loc])
    except:
        ytry = str(regs[y[loc]])
    
    curr_instruc = instrucs[loc]
    if curr_instruc == 'set':
        regs[x[loc]] = int(ytry)
        loc += 1
    elif curr_instruc == 'add':
        regs[x[loc]] += int(ytry)
        loc += 1
    elif curr_instruc == 'mul':
        regs[x[loc]] = regs[x[loc]] * int(ytry)
        loc += 1
    elif curr_instruc == 'mod':
        regs[x[loc]] = regs[x[loc]] % int(ytry)
        loc += 1
    elif curr_instruc == 'snd':
        
        last_sent = regs[x[loc]]
        loc += 1
    elif curr_instruc == 'rcv':
        if regs[x[loc]] != 0:
            done = True
        loc += 1
    else:
        if regs[x[loc]] > 0:
            loc += int(ytry)
        else:
            loc += 1
    if loc >= len(instrucs) or loc < 0:
        done = True
   
print(last_sent) # part1
#copying and pasting part 1 code below for part 2 to keep them separate.
def contuntilsend(regs, loc, instrucs, x, y, inputque, count):
    done = False
    sent = []
    
    while done == False:
        
        try: 
            ytry = int(y[loc])
        except:
            ytry = str(regs[y[loc]])

        curr_instruc = instrucs[loc]
        if curr_instruc == 'set':
            regs[x[loc]] = int(ytry)
            loc += 1
        elif curr_instruc == 'add':
            regs[x[loc]] += int(ytry)
            loc += 1
        elif curr_instruc == 'mul':
            regs[x[loc]] = regs[x[loc]] * int(ytry)
            loc += 1
        elif curr_instruc == 'mod':
            regs[x[loc]] = regs[x[loc]] % int(ytry)
            loc += 1
        elif curr_instruc == 'snd':
            sent.append(regs[x[loc]])
            loc += 1
            count += 1     
        elif curr_instruc == 'rcv':
            if len(inputque) > 0:
                regs[x[loc]] = inputque.pop(0)
                loc += 1
            else:
                done = True
                return regs, sent[:], loc, count, True
        else:
            try:
                
                if regs[x[loc]] > 0:
                    loc += int(ytry)
                else:
                    loc += 1
            except:
                loc += int(ytry)
        if loc >= len(instrucs) or loc < 0:
           
            done = True
            return regs, sent[:], loc, count, False
        

            
asc = 97
regs0 = {}
for z in range(16):
    regs0[str(unichr(asc))] = 0  
    asc += 1
regs1 = {}
asc = 97
for z in range(15):
    regs1[str(unichr(asc))] = 0  
    asc += 1
regs1['p'] =1
leftright = True
conleft = True
conright = True
leftloc = 0
rightloc = 0
leftinput = []
rightinput = []
leftcount = 0
rightcount = 0
first = True
while conleft or conright:
   
    if leftright and (len(leftinput) > 0 or first):
        regs0, temp, leftloc, leftcount, conleft = contuntilsend(regs0, leftloc, instrucs, x, y, leftinput, leftcount)
        rightinput += temp
        leftright = False
        first = False
    elif len(rightinput) > 0:
        
        regs1, temp, rightloc, rightcount, conright = contuntilsend(regs1, rightloc, instrucs, x, y, rightinput, rightcount)
        leftinput += temp
        leftright = True
    else:
        conleft = False
        conright = False
print(rightcount)
        
        

    
    
    