good = 0
for n in range(138241,674035):
    s = str(n)
    pair = False
    incr = True
    for i in range(5):
        if s[i] == s[i+1]: pair = True
        if s[i] > s[i+1]: incr = False
    if pair and incr: good += 1

print(good)
