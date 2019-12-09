import intcode
with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]

prog = [int(x) for x in csv[0]]
m = intcode.machine(prog)
m.put(1)
m.run()
print(m.get())
m = intcode.machine(prog)
m.put(2)
m.run()
print(m.get())
