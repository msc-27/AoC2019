good = 0
for n in range(138241,674035):
    s = str(n)
    pair = False
    incr = True
    for i in range(5):
        if s[i] == s[i+1]:
            cand = True
            if i > 0 and s[i-1] == s[i]: cand = False
            if i < 4 and s[i+2] == s[i]: cand = False
            pair = pair or cand
        if s[i] > s[i+1]: incr = False
    if pair and incr: good += 1

print(good)
