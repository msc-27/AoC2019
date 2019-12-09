with open('input') as f:
    inp = f.read().strip()

out = 0
layers = []
for x in range(0,len(inp),150):
    layers.append(inp[x:x+150])

minz_layer = sorted(layers, key=lambda x:x.count('0'))[0]
out = minz_layer.count('1') * minz_layer.count('2')
print(out)

msg = ''
for y in range(6):
    for x in range(25):
        i = 0
        while layers[i][y*25+x] == '2': i += 1
        pix = layers[i][y*25+x]
        msg += '*' if pix == '1' else ' '
    msg += '\n'
print(msg)
