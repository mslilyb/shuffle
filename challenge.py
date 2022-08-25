
import sys

print(sys.argv[])

fp = open(sys.argv[2])
lines = []

for line in fp.readlines():
    print(line)
    lines.append(line)



print(lines)

fp.close()
