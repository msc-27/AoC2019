import intcode
with open('input') as f:
    lines = [x.strip('\n') for x in f]
csv = [x.split(',') for x in lines]

prog = [int(x) for x in csv[0]]
m = intcode.machine(prog)

f = open('instr','r')
for line in f:
    for c in line:
        m.put(ord(c))
    m.run()
    msg = ''
    v = m.get()
    while v != None:
        msg += chr(v)
        v = m.get()
print(msg)
items = ['monolith','weather machine','mutex','hologram','polygon','jam','semiconductor','prime number']
import itertools
for i in range(1,9):
    for comb in itertools.combinations(items,i):
        for item in comb:
            instr = 'take ' + item
            for c in instr: m.put(ord(c))
            m.put(10)
        for c in 'north': m.put(ord(c))
        m.put(10)
        for item in comb:
            instr = 'drop ' + item
            for c in instr: m.put(ord(c))
            m.put(10)
m.run()
msg = ''
v = m.get()
while v != None:
    msg += chr(v)
    v = m.get()
print(msg)
