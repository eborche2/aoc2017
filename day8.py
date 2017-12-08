
def process(loc, plus_minus, amount, condition, regs):   
    left = condition[:condition.index(' ')]
    temp = condition[condition.index(' ')+1:]
    mid = temp[:temp.index(' ')]
    val_right = int(temp[temp.index(' ')+1:])
    val_left = regs[left]
    check = False
    to_eval = 'if %s %s %s: check = True' % (val_left, mid, val_right)
    exec(to_eval)
    if check:
        to_change = regs[loc]
        if plus_minus == 'inc':
            to_change += amount
        else:
            to_change -= amount
        regs[loc] = to_change

    
with open('file8.in') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

regs = {}
instrucs = []
current_max = None
for each in content:
    regs[each[0:each.index(' ')]] = 0  
for each in content:
    loc = each[0:each.index(' ')]
    plus_minus = each[each.index(' ')+1: each.index(' ')+4]
    temp = each[each.index(' ')+1:]
    temp = temp[temp.index(' ')+1:]
    amount = int(temp[:temp.index(' ')])
    for x in range(2):
        temp = temp[temp.index(' ')+1:]
    
    process(loc, plus_minus, amount, temp, regs)
    check_max = regs[max(regs, key=regs.get)]
    if current_max:
        if check_max > current_max:
            current_max = check_max
    else:
        current_max = check_max
    
max_loc = max(regs, key=regs.get)
print(regs[max_loc])# part 1
print(current_max)# part 2
    
