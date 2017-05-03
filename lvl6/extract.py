import sys
import os

from os.path import basename
from os.path import splitext

infile = sys.argv[1] if len(sys.argv) > 1 else 'testInput.txt'
outdir = 'graphs-%s' % splitext(basename(infile))[0]

if not os.path.exists(outdir):
    os.makedirs(outdir)

# parse file
with open(infile) as f:
    n_line = f.readline()
    N = int(n_line)
    for n in xrange(N):
        outfile = "%s/%d.txt" % (outdir, n+1)
        with open(outfile, 'w') as out:
            out.write('1\n')
            tokens_line = f.readline()
            out.write(tokens_line)
            tokens = tokens_line.split(' ')
            F = int(tokens[0])
            S = int(tokens[1])
            for _ in xrange(S):
                tokens = f.readline()
                out.write(tokens)
