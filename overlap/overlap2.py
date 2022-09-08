import sys

def overlap(f1, f2):
    if f1.beg <= f2.end and f1.end >= f2.beg: return True
    else: return False

class Feature:
    def __init__(feat, beg, end):
        feat.beg = beg
        feat.end = end

chrs = {}
seen = {}

with open(sys.argv[2]) as file2:
    while True:
        line = file2.readline()
        if line == "": break
        line = line.split()
        chrom = line[0]
        feat = Feature(line[1], line[3])
        if chrom not in chrs: chrs[chrom] = []
        chrs[chrom].append(feat)


with open(sys.argv[1]) as file1:
    while True:
        line1 = file1.readline()
        if line1 == "": break
        chr, beg, __, end = line1.split()
        f1 = Feature(beg, end)

        for f in chrs[chr]:
            if overlap(f1, f):
                print(f'{chr} {f1.beg} - {f1.end} overlaps {chr} {f.beg} - {f.end}')
