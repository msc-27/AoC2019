import intcode
with open('input','r') as f:
    prog = [int(x) for x in f.read().strip().split(',')]
m = intcode.machine(prog, lambda :1)
m.run()
print()
m.reset(prog, lambda :5)
m.run()
