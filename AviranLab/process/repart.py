import gzip
import json
import math
from subprocess import run
import sys

def twod_edist(mu, mp, pu, pp):
    return math.sqrt((pu - mu) ** 2 + (pp - mp) ** 2)

def read_fasta(filename):

	if   filename == '-':          fp = sys.stdin
	elif filename.endswith('.gz'): fp = gzip.open(filename, 'rt')
	else:                          fp = open(filename)

	name = None
	seqs = []

	while True:
		line = fp.readline();
		if line == '': break
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				yield(name, ''.join(seqs))
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)

	yield(name, ''.join(seqs))
	fp.close()


outpath = '~/Code/shuffle/AviranLab/testouts/invivo/repart'
shapef = "_repart.shape"
faf = "_repart.fa"
repart = "_repart"
partnum = int(sys.argv[1])
startmodel = sys.argv[2]
genome = sys.argv[3]
shapefile = sys.argv[4]

expansions = int(sys.argv[5]) #lets start with 30

exd = 150

startcoord = (300 * partnum)
endcoord = startcoord + 300


for f, s in read_fasta(genome):
    seq = s

for sh, se in read_fasta(shapefile):
    shapes = se

modelfp = open(startmodel)

initialmodel = json.load(modelfp)

initialup, initialp = initialmodel['structure_model']['A'][0][0], initialmodel['structure_model']['A'][1][0]

sd = list(shapes)
resultfp = open("newdists", 'w')

for exn in range(expansions + 1):
	offset = exn * exd
	newstart = startcoord - offset

	repartseq = seq[newstart:endcoord + offset]
	rptshape = sd[newstart:endcoord + offset]

	repartshape = ''.join(rptshape)

	shapeout = str(exn) + shapef
	faout = str(exn) + faf

	shfp = open(shapeout, 'w')
	fafp = open(faout, 'w')

	shfp.write(f'>{exn}\n{repartshape}')
	shfp.close()
	fafp.write(f'>{exn}\n{repartseq}')
	fafp.close()
	testdir = str(exn) + repart + "big"

	run(f'patteRNA ~/Code/shuffle/AviranLab/testouts/invivo/repart/bigdata/{shapeout} ~/Code/shuffle/AviranLab/testouts/invivo/repart/{testdir}/HDSL -v -f ~/Code/shuffle/AviranLab/testouts/invivo/repart/bigdata/{faout}', shell=True)

	newfp =  f'/home/ashtoreth/Code/shuffle/AviranLab/testouts/invivo/repart/{testdir}/HDSL/trained_model.json'
	with open(newfp) as nfp:
		newmodel = json.load(nfp)

	newup, newp = newmodel['structure_model']['A'][0][0], newmodel['structure_model']['A'][1][0]

	dist = twod_edist(initialup, initialp, newup, newp)
	resultfp.write(f'{dist}\n')



resultfp.close()
