import sys

def architect(s, c, d):

    ori_s = s
    ori_d = d
    pieces = 0

    if c < 4:
        return 0

    if s == 0 and d == 0:
        return 4

    if s == 1 and c < 8:
        return 4 + d-d%2
    elif s == 1 and c >= 8:
        return 4 + d-d%2 + c/2

    # outer space
    c -= 4
    pieces += 4

    while c >= 8 and d >= 1:
        c -= 8
        d -= 1
        pieces += 9

    l1 = 0
    l2 = 0

    # spend D's assap
    # we can use D's compensating with S's
    if d > 1:
        pieces += d - d%2
        l1 = d/2 * 2
        d = d%2

    # try to spend the last D
    if d >= 1 and s >= 2:
        pieces += 3
        d = 0
        s -= 2
        l1 += 2

    #while d > 0 and s >= 2:
    #    s -= 2
    #    d -= 1
    #    pieces += 3

    if s > 1:
        pieces += s - s%2
        l1 += s/2
        s = s%2

    while c >= 2 and max(l1, l2) > 0:
        c -= 2
        pieces += 2

    #print 'S=%d, C=%d, D=%d' % (s, c, d)
    return pieces

# parse file
infile = sys.argv[1] if len(sys.argv) > 1 else 'debugInput.txt'
with open(infile) as f:
    N = int(f.readline())
    for n in xrange(1, N+1):
        tokens = (int(x) for x in f.readline().split(' '))
        value = architect(*tokens)
        print 'Case #%d: %d' % (n, value)
