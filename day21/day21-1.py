import intcode
with open('input') as f:
    lines = [x.strip('\n') for x in f]
csv = [x.split(',') for x in lines]
prog = [int(x) for x in csv[0]]
m = intcode.machine(prog)
for c in 'OR A T\n':
    m.put(ord(c))
for c in 'AND B T\n':
    m.put(ord(c))
for c in 'AND C T\n':
    m.put(ord(c))
for c in 'NOT T J\n':
    m.put(ord(c))
for c in 'AND D J\n':
    m.put(ord(c))
for c in 'WALK\n':
    m.put(ord(c))
m.run()
# Jump if the landing spot (D) is ground, and there is a reason to jump:
# any of the next three tiles is a hole.

msg = ''
v = m.get()
while v != None:
    if v < 256: msg += chr(v)
    if v >= 256:
        msg += '\n' + str(v) + '\n'
    v = m.get()
print(msg)
