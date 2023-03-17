import sys
import statistics

files = sys.argv[1:]

reacts = files[0]
loops = files[1]
mean = files[2]
max = files [3]

mefp = open(mean)
mafp = open(max)

me = float(mefp.readline().strip())
print(me)
ma = float(mafp.readline().strip())

mefp.close()
mafp.close()

lfp = open(loops)

below = []
above = []
print(me)

with open(reacts) as rfp:
    linecount = 0
    for line in rfp:
        line.strip()
        print(line)

        if float(line) >= me:
            print(me)
            below.append(f'{line}\t{linecount}')
        linecount += 1

print(below)
wfp = open("outfile", 'w')
for val in below:
    wfp.write(f'{val}\n')

wfp.close()
