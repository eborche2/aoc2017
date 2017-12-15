def makeeven_bits(tomake):
    if len(tomake) < 32:
        at_start = ''
        to_add = 32 - len(tomake)
        for each in range(to_add):
            at_start += '0'
        tomake = at_start + tomake
    return tomake
def thiscouldbebad(x, factor, divisor, orig):
    if x % divisor == 0:
        return x
    else:
        x = (x * factor) % orig
        return thiscouldbebad(x, factor, divisor, orig)
gena_factor = 16807
genb_factor = 48271
divisor = 2147483647
start_a = 783 #example 65
start_b = 325 #example 8921
count = 0
for x in range(5000000):
    start_a = (start_a * gena_factor) % divisor
    start_b = (start_b * genb_factor) % divisor
    start_a = thiscouldbebad(start_a, gena_factor, 4, divisor)
    start_b = thiscouldbebad(start_b, genb_factor, 8, divisor)
    first_a = '{0:b}'.format(start_a)
    first_b = '{0:b}'.format(start_b)
    first_a = makeeven_bits(first_a)[16:]
    first_b = makeeven_bits(first_b)[16:]
    if first_a == first_b:
        count += 1
print(count) #part1 comment out the method on line 24 25