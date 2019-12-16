with open('input') as f:
    data = f.read().strip()

def patt(n):
    while True:
        for i in range(n): yield 0
        for i in range(n): yield 1
        for i in range(n): yield 0
        for i in range(n): yield -1

inp = [int(c) for c in data]

for i in range(100):
    newinp = []
    for j in range(len(inp)):
        pgen = patt(j+1)
        _ = next(pgen)
        val = 0
        for k in range(len(inp)):
            val += inp[k] * next(pgen)
        newinp.append(abs(val)%10)
    inp = newinp

out = ''
for i in range(8): out += str(inp[i])
print(out)
