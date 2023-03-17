import sys
import statistics

def trimoutliers(data):
    quants = statistics.quantiles(data)

    q1 = quants[0]
    q3 = quants[2]

    iqr = q3 - q1

    lcut = q1 - (1.5 * iqr)
    rcut = q3 + (1.5 * iqr)
    print(quants)
    print(lcut, rcut)
    outliers = []
    keeps = []

    for i in range(len(data)):
        outliar = False
        side = None
        if data[i] < lcut:
            outliar = True
            side = 'Below IQR'

        elif data[i] > rcut:
            outliar = True
            side = 'Above IQR'

        if side != 'Above IQR':
            keeps.append(data[i])

        if outliar:
            outliers.append({'partition' : i, 'side' : side, 'edist' : data[i]})

    return outliers, keeps


file = sys.argv[1]
reacts = []

with open(file) as fp:
    for line in fp:
        line.strip()
        reacts.append(float(line))


outl, kept = trimoutliers(reacts)
above = 0
below = 0

for out in outl:
    if out['side'] == 'Above IQR':
        above += 1
    else:
        below += 1

print("# of outliers:", len(outl), above, "above", below, "below")

while len(outl) != 0:
    outl, kept = trimoutliers(kept)
    above = 0
    below = 0

    for out in outl:
        if out['side'] == 'Above IQR':
            above += 1
        else:
            below += 1

    print("# of outliers:", len(outl), above, "above", below, "below")

print("New mean:", statistics.mean(kept), "New min:", min(kept), "New max:", max(kept))

with open("outliarless", 'a') as wfp:
    for entry in kept:
        wfp.write(f'{entry}\n')
