with open('file23.in') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

regs = {}
instrucs = []
x = []
y = []
asc = 97
for z in range(8):
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
count = 0

ffs = 0
fs = []
switch = False
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
    elif curr_instruc == 'sub':
        regs[x[loc]] -= int(ytry)
        loc += 1
    elif curr_instruc == 'mul':
        regs[x[loc]] = regs[x[loc]] * int(ytry)
        loc += 1
        count += 1
    elif curr_instruc == 'mod':
        regs[x[loc]] = regs[x[loc]] % int(ytry)
        loc += 1
    elif curr_instruc == 'snd':
        
        last_sent = regs[x[loc]]
        loc += 1
    elif curr_instruc == 'rcv':
        loc += 1
    else:
        try:
                
            if regs[x[loc]] != 0:
                loc += int(ytry)
            else:
                loc += 1
        except:
            loc += int(ytry)
    if loc >= len(instrucs) or loc < 0:
        done = True
    
   
def is_prime(a):
    return all(a % i for i in xrange(2, a))        
print(count) # part 1
#part 2 Realized pretty quick there was no way the code above would finish
# Broke down the pattern from the input and eventually determined the core parts.
h = 0
b = 107900
c = 124900
while b <= c:
    if not is_prime(b):
        h += 1
    b += 17 

print(h)


        

