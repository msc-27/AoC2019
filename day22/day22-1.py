with open('input') as f:
    lines = [x.strip('\n') for x in f]
ssv = [x.split(' ') for x in lines]

deck = list(range(10007))
for line in ssv:
    if line[0] == 'cut':
        n = int(line[1])
        if n < 0: n = len(deck) + n
        deck = deck[n:] + deck[:n]
    if line[0] == 'deal' and line[1] == 'into':
        deck = deck[::-1]
    if line[0] == 'deal' and line[1] == 'with':
        newdeck = deck.copy()
        incr = int(line[3])
        pos = 0
        for i in range(len(deck)):
            newdeck[pos] = deck[i]
            pos += incr
            pos %= len(deck)
        deck = newdeck
print(deck.index(2019))
