class node(object):
    
    def __init__(self, name, weight, above):
        self.name = name
        self.weight = weight
        self.above = above
        self.below = []
        
    def getweight(self):
        return self.weight
    
    def getabove(self):
        return self.above
    
    def getname(self):
        return self.name
    
    def getbelow(self):
        return self.below
    
    def setbelow(self, toadd):
        self.below.append(toadd)
       
with open('file4.in') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
nodes = []
aboves = []
rotation = []
for each in content:
    name = each[0:each.index(' ')]
    weight = each[each.index('(') + 1: each.index(')')]
    above = []
    if each.find('>') > 0:
        theabove = each[each.find('>') + 1:]
        comma = True
        while comma:
            if theabove.find(',') > 0:
                above.append(theabove[1: theabove.find(',')])
                theabove = theabove[theabove.find(',')+1: ]
            else:
                above.append(theabove[1:])
                comma = False 
    nodes.append(node(name, weight, above))
    aboves.append(above)
for x, each in enumerate(aboves):
    for toadd in each:
        for thisnode in nodes:
            if toadd == thisnode.getname():
                thisnode.setbelow(nodes[x].getname())
                break
for each in nodes:
    if len(each.getbelow()) == 0:
        print(each.getname())#Part 1
        rotation = each.getabove()


def getnode(nodes, name):
        for each in nodes:
            if each.getname() == name:
                return each   
def recur_add(node, total):
        total += int(node.getweight())
        for each in node.getabove():
            total += recur_add(getnode(nodes, each), 0)
        return total
previous = None


def balance(rotation, previous):
    more = False
    row = []
    totals = []
    done = False
    for each in rotation:
        row.append(getnode(nodes, each))
        if len(getnode(nodes,each).getabove()) > 0:
            more = True     
    for each in row:
        totals.append(recur_add(each, 0))   
                                  
    if not more:
        done = True
        print(previous)
    
    for x, each in enumerate(totals):
        if x +1 == len(totals):
            done = True
            print(previous)
            break
        elif each != totals[x+1]:
            count1 = totals.count(each)
            count2 = totals.count(totals[x+1])
            if count1 > count2:
                diff = each - totals[x+1]
                previous = int(row[x+1].getweight()) + diff
                current = x +1
                print(previous, ' ', diff, ' ', row[x+1].getname())
                break
            else:
                diff = totals[x+1] - each
                previous = int(row[x].getweight()) + diff
                current = x
                print(previous, ' ', diff, ' ', row[x].getname())
                break
           
    del rotation[:]
    if not done:
        rotation += row[current].getabove()
        balance(row[current].getabove(), previous)
    if len(rotation) == 0:
        done = True
        for each in row:
            balance(rotation, previous)
balance(rotation, previous)      
#The last previous which prints on the screen is the right answer... 
