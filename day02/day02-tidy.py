import intcode
with open('input','r') as f:
    data = f.read().strip().split(',')
m = intcode.machine(int(x) for x in data)
m.poke(1,12)
m.poke(2,2)
m.run()
print(m.peek(0))
