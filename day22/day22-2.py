with open('input') as f:
    lines = [x.strip('\n') for x in f]
ssv = [x.split(' ') for x in lines]

# Bring in some code for arithmetic mod p
# Begin code lifted from the Internet
def egcd(a,b):
    if a == 0:
        return (b,0,1)
    else:
        g,y,x = egcd(b%a,a)
        return (g,x-(b//a)*y,y)
def modinv(a,m):
    g,x,y = egcd(a,m)
    return x%m
# End code lifted from the Internet

def modexp(a,b,p): # Calculate a^b mod p
    r = 1
    power = a
    while b:
        if b % 2 == 1: r = (r * power) % p
        power = (power * power) % p
        b //= 2
    return r

p = 119315717514047 # deck size (assumed prime)
N = 101741582076661 # number of shuffles

# Function to perform a reverse shuffle, so that we can track where a
# particular card came from before the shuffle.
# Observe that in terms of modulo arithmetic, a 'cut' is a subtraction
# operation and a 'deal with increment' is a multiplication operation.
# The reverse shuffle therefore turns these into additions and
# multiplication by inverses respectively, mod p.
def revshuf(pos):
    for line in ssv[::-1]:
        if line[0] == 'cut':
            n = int(line[1])
            pos += n
            pos %= p
        if line[0] == 'deal' and line[1] == 'into':
            pos = p - pos - 1
        if line[0] == 'deal' and line[1] == 'with':
            incr = int(line[3])
            pos = pos * modinv(incr,p)
            pos %= p
    return pos

# The entire sequence of steps can be reduced to a single linear function:
# shuf(x) = Ax + b (mod p)
# The reverse shuffle, likewise:
# revshuf(x) = Cx + d (mod p)
# We wish to find C and d, and hence calculate revshuf^N(2020), where N
# is the number of shuffles performed (defined above)
# d = revshuf(0)
# C = revshuf(1) - d

# revshuf^2(x) = C^2.x + Cd + d
# revshuf^3(x) = C^3.x + C^2.d + Cd + d
# revshuf^N(x) = C^N.x + d( 1 + C + C^2 + ... + C^(N-1) )

# To get the tricky term:
# s = 1 + C + C^2 + ... + C^(N-1)
# Cs = C + C^2 + C^3 + ... + C^N
# Cs-s = C^N - 1
# s = inv(C-1) . (C^N - 1)

# So let's do this!

d = revshuf(0)
C = revshuf(1) - d
s = (modinv(C-1,p) * (modexp(C,N,p) - 1)) % p

term1 = (modexp(C,N,p) * 2020) % p
term2 = (d * s) % p
answer = (term1 + term2) % p
print(answer)
