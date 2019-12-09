with open('input') as f:
    lines = [x.strip() for x in f]

out = 0
layers = []
for x in range(0,len(lines[0]),150):
    layers.append(lines[0][x:x+150])

zeros = [x.count('0') for x in layers]
i = zeros.index(min(zeros))
out = layers[i].count('1') * layers[i].count('2')
print(out)

pix = []
for y in range(6):
    for x in range(25):
        i = 0
        while layers[i][y*25+x] == '2': i += 1
        pix.append(layers[i][y*25+x])

i = 0
msg = ''
for y in range(6):
    for x in range(25):
        msg += '*' if pix[i] == '1' else ' '
        i += 1
    msg += '\n'
print(msg)
