import itertools
import sys

def validtriangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

infile = sys.argv[1] if len(sys.argv) > 1 else 'testInput.txt'
with open(infile) as f:
    lines = f.readlines()
    n = lines[0]
    for i, line in enumerate(lines[1:]):
        tokens = line.split(' ')
        n = int(tokens[0])
        l = [int(x) for x in tokens[1:]]
        candidate = 0
        for comb in itertools.combinations(l, 3):
            if validtriangle(*comb):
                perim = sum(comb)
                if candidate == 0 or perim < candidate:
                    candidate = perim
        sol = 'IMPOSSIBLE' if candidate == 0 else candidate
        print 'Case #%d: %s' % (i+1, sol)
