# Originally done by manually adjusting required quantity of FUEL and
# repeatedly running the Part 1 program until ore_needed exceeded 1 trillion
# Interval bisection method now written to do this automatically

STOCK = 1000000000000

from collections import defaultdict
with open('input') as f:
    lines = [x.strip() for x in f]

bom = dict() # Bill of materials
for line in lines:
    srcs,targ = line.split('=>')
    tqs,to = targ.strip().split(' ')
    tq = int(tqs)
    srcl = []
    for src in srcs.split(','):
        sqs,so = src.strip().split(' ')
        sq = int(sqs)
        srcl.append((sq,so))
    bom[to] = (tq,srcl) # Base quantity, component list

def get_ore_needed(fuel_quantity):
    req = [('FUEL',fuel_quantity)]
    surplus = defaultdict(int)
    ore_needed = 0
    
    while req:
        chem, qty = req.pop(0)
        if chem == 'ORE':
            ore_needed += qty
            continue
        in_hand = min(qty, surplus[chem])
        surplus[chem] -= in_hand
        qty -= in_hand
        bq, srcs = bom[chem]
        mult = qty / bq
        if mult != int(mult): mult += 1
        mult = int(mult)
        for src in srcs:
            req.append((src[1], mult * src[0]))
        surplus[chem] += bq * mult - qty
    return ore_needed

def test_ore_needed(fuel_quantity):
    n = get_ore_needed(fuel_quantity)
    if n < STOCK:
        return 0
    else:
        return 1

ore_for_1 = get_ore_needed(1)
guess = STOCK // ore_for_1
mult = 2
while not test_ore_needed(guess * mult): mult += 1
low = guess * (mult-1)
high = guess * mult
while high - low != 1:
    trial = (low + high) // 2
    if test_ore_needed(trial):
        high = trial
    else:
        low = trial
print(low)
