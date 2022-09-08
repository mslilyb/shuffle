import sys
import random


count = int(sys.argv[1])
chcount = int(sys.argv[2])
chlen = int(sys.argv[3])
j = 0

for i in range(count):
    chrom = random.randrange(1, chcount, 1)
    beg = random.randrange(1, chlen, 1)
    end = random.randrange(beg, chlen, 1)
    print(f'Chr{chrom}: {beg} - {end}')
