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
for c in 'OR E T\n':
    m.put(ord(c))
for c in 'OR H T\n':
    m.put(ord(c))
for c in 'AND T J\n':
    m.put(ord(c))
for c in 'RUN\n':
    m.put(ord(c))
m.run()
# In addition to the conditions for Part 1, we also check that it is safe to
# land at D: either E or H needs to be ground so that the springdroid can
# safely run ahead or jump again.
# After the Part 1 program section, T is FALSE if a jump is being triggered,
# so we can use that fact to treat 'OR E T' as a 'set value' operation.

msg = ''
v = m.get()
while v != None:
    if v < 256: msg += chr(v)
    if v >= 256:
        msg += '\n' + str(v) + '\n'
    v = m.get()
print(msg)
