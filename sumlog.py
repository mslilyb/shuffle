# numpy.logaddexp2()

import math

def sumlog2(a, b, mag = 30):

	if abs(a - b) > mag: return max(a, b)
	#return math.log2(1 + 2**(b-a) +_ a)
	ma = a - a
	mb = b - a
	pa = 2**ma
	pb = 2**mb
	sp = pa + pb
	ld = math.log2(sp)
	ld += a

	print (ld)

a = -9999
b = -9997


sumlog2(a, b)