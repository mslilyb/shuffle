import sys
import math
from scipy.spatial.distance import euclidean


def makelist(filename):
    fp = open(filename)

    list = []
    for line in fp:
        if line.startswith('>'):
            continue

    splitline = line.strip().split(' ')

    for element in splitline:
        list.append(float(element))
    fp.close()
    return list

def findmax(distlist):
    return max(distlist), distlist.index(max(distlist))

def findmin(distlist):
    return min(distlist), distlist.index(min(distlist))





fullpostfile = sys.argv[1]
postfiles = sys.argv[2]




mfp = open(fullpostfile)

pfp = open(postfiles)

mposts = makelist(fullpostfile)
partposts = []
parts = []

for line in pfp:
    part = line.strip()
    posts = makelist(part)

    partposts.append(posts)
    parts.append(part.split('/')[-3])

edists = []


for i in range(len(partposts)):
    startcoord = i * 300
    cvector = mposts[startcoord:startcoord + 300]

    if len(cvector) != len(partposts[i]):
        print("Error! Mismatch Vectors!")
        break

    edists.append(euclidean(cvector, partposts[i]))


maxdist, partloc = findmax(edists)

partmax = parts[partloc]

mindist, partloc = findmin(edists)

partmin = parts[partloc]

print("Posterior Distance Results:")

print(f'Partition\tDistance')

for partish, dist in zip(parts, edists):
    print(f'{partish}\t{dist}')


print(f'max\t{partmax}\t{maxdist}')
print(f'min\t{partmin}\t{mindist}')







mfp.close()
pfp.close()
