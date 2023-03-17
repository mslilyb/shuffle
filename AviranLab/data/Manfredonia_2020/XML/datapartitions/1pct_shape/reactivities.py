import sys
import statistics
import math

plot = sys.argv[1]

masterfile = sys.argv[2]


partfiles = sys.argv[3:]


def plotreacts():
    return None




mfp = open(masterfile)
mzeros = 0
nanvals = ['NaN', 'nan', 'NAN']
mreactivities = []

for line in mfp:
    if line.startswith('>'): continue
    else:
        vals = line.rstrip().split(' ')

        for val in vals:
            if val == 'NaN' or val == 'nan' or math.isclose(float(val), 0.000):
                mzeros += 1
            else:
                mreactivities.append(float(val))
print("Full", "Mean:", statistics.mean(mreactivities), "Median:", statistics.median(mreactivities), "Max:", max(mreactivities), "Min:", min(mreactivities), "Zeroes:", mzeros)

mfp.close()

for file in partfiles:
    pfp = open(file)

    zeros = 0
    reacts = []

    for line in pfp:
        if line.startswith('>'): continue
        else:
            vals = line.rstrip().split(' ')

            for val in vals:
                if val == 'NaN' or val == 'nan' or math.isclose(float(val), 0.0000):
                    zeros += 1
                else:
                    reacts.append(float(val))

    print(file.strip('.shape'), "Mean:", statistics.mean(reacts), "Median:", statistics.median(reacts), "Max:", max(reacts), "Min:", min(reacts), "Zeroes:", zeros)
    pfp.close()
