import intcode
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]

total = 0
prog = [int(x) for x in csv[0]]
m = intcode.machine(prog)
m.run()
t = m.get()
t = m.get()
t = m.get()
while t != None:
    if t == 2: total += 1
    t = m.get()
    t = m.get()
    t = m.get()
print(total)
