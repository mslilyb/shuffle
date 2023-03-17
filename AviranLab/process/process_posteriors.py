import sys

fname = sys.argv[1]
obs = []

with open(fname, 'r') as fp:
    while True:
        name = fp.readline()
        if not name: break
        obs.append(fp.readline().strip().split(' '))

revobs = []

for i in range(len(obs)):
    revobs.append(obs[i])
    for j in range(len(revobs[i])):
        revobs[i][j] = round(1 - float(revobs[i][j]), 4)

print(revobs[0][900:1030])
