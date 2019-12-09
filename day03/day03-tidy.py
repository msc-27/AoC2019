with open('input') as f:
    lines = [x.strip() for x in f]
csv = [x.split(',') for x in lines]

step = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
def makedict(moves):
    x,y = 0,0
    steps = 0
    ret = dict()
    for move in moves:
        direction = move[0]
        size = int(move[1:])
        dx,dy = step[direction]
        for i in range(size):
            x += dx; y += dy
            steps += 1
            if (x,y) not in ret: ret[(x,y)] = steps
    return ret

def dist(p): return abs(p[0]) + abs(p[1])
wires = list(map(makedict, csv))
inters = set.intersection(*(set(w) for w in wires))
print(min(dist(i) for i in inters))
print(min(sum(w[i] for w in wires) for i in inters))
