import intcode_1 as intcode
with open('input','r') as f:
    prog = [int(x) for x in f.read().strip().split(',')]
m = intcode.machine(prog)
m.run()
