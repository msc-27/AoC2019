with open('input') as f:
    data = f.read().strip()
inp = [int(c) for c in data]

ilen = len(inp)
offset = int(data[:7])

# Find the tail of the signal, starting from the offset
start = offset % ilen            # find input position aligned with offset
inp = inp[start:] + inp[:start]  # rotate input to start here
tail_len = ilen * 10000 - offset # length of tail
repeats = tail_len // ilen       # number of full repeats of input in tail
leftover = tail_len % ilen       # number of digits left over in tail

tail = inp * repeats + inp[:leftover]

# In the tail, element k of phase j+1 is equal to
# the sum of the elements k...N in phase j

for i in range(100):
    newtail = []
    val = sum(tail)
    val %= 10
    for j in range(tail_len):
        newtail.append(val)
        val -= tail[j]
        val %= 10
    tail = newtail

out = ''
for i in range(8): out += str(tail[i])
print(out)
