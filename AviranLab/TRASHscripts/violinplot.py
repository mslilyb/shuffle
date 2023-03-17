import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
import statistics



reacts = sys.argv[1]


fp = open(reacts)

reactlist = []

for line in fp:
    line.strip()
    reactlist.append(float(line))

avg = statistics.mean(reactlist)
median = statistics.median(reactlist)
max = max(reactlist)
min = min(reactlist)


fig, ax = plt.subplots()
fig.subplots_adjust(top=0.88,
bottom=0.11,
left=0.45,
right=0.75,
hspace=0.2,
wspace=0.2)

ax.violinplot(reactlist, showmeans=True, showmedians=True)

ax.text(0.75,0.14, f'avg = {avg:.3f}, med = {median:.3f}\nmax = {max:.3f}, min = {min:.3f}')
ax.set_ylabel('euclidean distance')
plt.show()
