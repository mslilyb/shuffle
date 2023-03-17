import sys


file = sys.argv[1]

fp = open(file)

line = fp.readline()
line = fp.readline()
line = fp.readline()

subseqs = []

for i in range(0, len(line), 300):
    subseqs.append(line[i:i+300])

fp.close()

stcounts = []
open = False
closed = True
closeseen = False
openseen = False
need = 0
loops = 0


for subseq in subseqs:
    for pos in subseq:
        if pos == '(':
            if closed:
                open = True
                need += 1
                openseen = True
                closed = False
            elif openseen == True and closed == False:
                 continue
            elif openseen == False and closed == False:
                need += 1

        elif pos == '.':
            openseen = False
            closeseen = False

        elif pos == ')':
            if closed == True:
                continue

            elif closeseen == False:
                need -= 1
                loops += 1
                closeseen = True

                if need == 0:
                    closed = True

    stcounts.append(loops)
    loops = 0

print("Average Loops per sequence:", sum(stcounts)/100)
print("Max:", stcounts.index(max(stcounts)), max(stcounts))
print("Min:", stcounts.index(min(stcounts)), min(stcounts))

for i in range(len(stcounts)):
    print(i, stcounts[i])
