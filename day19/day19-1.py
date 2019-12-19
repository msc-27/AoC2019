import intcode
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]
prog = [int(x) for x in csv[0]]

out = 0
for y in range(50):
    for x in range(50):
        m=intcode.machine(prog)
        m.put(x)
        m.put(y)
        m.run()
        v = m.get()
        out += v
print(out)
