import sys

fname = sys.argv[1]

#fp = open(fname)
linecount = 0

with open(fname, 'r') as fp:
    while True:
        nameline = fp.readline()
        if not nameline: break
        linecount += 1
        name = nameline.split('>')[1].strip()
        print(name)
        print(linecount)
