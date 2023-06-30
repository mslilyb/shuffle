#!/usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import sys
import argparse
import json

BASES = ('A', 'T', 'G', 'C', 'U', 'R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V', 'N')

PAIRING_TABLE = {'A': ('U', 'T'),
                 'U': ('A', 'G'),
                 'G': ('C', 'U', 'T'),
                 'C': ('G',),
                 'T': ('A', 'G')}

BRACKETS = ['()', '<>', '{}', '[]']  # Standard brackets, followed by alphabet (A<->a, B<->b, C<->c, etc.)
BRACKETS.extend([''.join((lb, rb)) for lb, rb in zip(string.ascii_uppercase, string.ascii_lowercase)])

LEFT_BRACKETS = set([pair[0] for pair in BRACKETS])
RIGHT_BRACKETS = set([pair[1] for pair in BRACKETS])
VALID_DB_CHAR = LEFT_BRACKETS | RIGHT_BRACKETS | set('.')

# Partner map is used to get both characters of a bracket when you have one
PARTNER_MAP = {lb: (lb, rb) for lb, rb in BRACKETS}  # Set up left brackets
PARTNER_MAP.update({rb: (lb, rb) for lb, rb in BRACKETS})  # Right brackets


def valid_db(db):
    """
    Checks if a given dot-bracket string is a valid structure (i.e., all opening bases
    have a matched closing pair and no closing pairs appear before an available opening
    pair has occurred).
    """

    # Check characters are all valid and note which brackets are present
    brackets = set()
    for s in db:
        if s not in VALID_DB_CHAR:
            return False
        if s == '.':
            continue
        else:
            brackets.add(''.join(PARTNER_MAP[s]))

    # Check validity of all bracket characters
    for lb, rb in brackets:

        # Skip bracket characters that aren't present
        if db.count(lb) == 0 and db.count(rb) == 0:
            continue

        # First, do a quick check if the number of brackets match up
        # (can detect most, but not all, invalid db with this)
        if db.count(lb) != db.count(rb):
            return False

        # Then, check that every right bracket is preceded by an available left bracket
        bracket_mask = np.array([(s == lb, s == rb) for s in db], dtype=bool)
        bracket_mask_cumsum = bracket_mask.cumsum(axis=0)

        # Return False if at any point there are more right brackets than left brackets
        if np.any(bracket_mask_cumsum[:, 1] > bracket_mask_cumsum[:, 0]):
            return False

    return True

def read_dot_bracket(fp, binary=False, with_sequence=False):
    """
        Returns a dictionary of structures (and sequences, if the with_sequence flag is set to True)
        for each transcript in a .dot file.

            Parameters:
                fp (str): Dot file
                binary (bool): Whether or not to return boolean state vectors.
                with_sequence (bool): Whether or not to return sequences in addition to structures.

            Returns:
                db_dict (dict): Dictionary of dot-bracket structures
                seq_dict (dict): Dictionary of nucleotide sequences
    """

    db_dict = dict()
    seq_dict = dict()

    with open(fp, 'r') as f:

        entry_name = None

        for line in f.readlines():

            if line[0] == '>':
                entry_name = line.split('>')[1].strip()
                continue

            if entry_name is not None:
                if line[0].upper() in BASES:
                    if with_sequence:
                        seq_dict[entry_name] = line.strip()
                    continue
                if line[0] in VALID_DB_CHAR:
                    if valid_db(line.strip()):
                        if binary:
                            db_dict[entry_name] = np.array([DB_MAP[d] for d in line.strip()], dtype=int)
                        else:
                            db_dict[entry_name] = line.strip()
                        entry_name = None
                else:
                    if line[0] in ('1', '0'):
                        if binary:
                            db_dict[entry_name] = np.array([DB_MAP[d] for d in line.strip()], dtype=int)
                            entry_name = None
                        else:
                            raise Exception('Binary references can only be read as binary paths.')
                    else:
                        raise Exception('Dot-bracket structure for transcript ""{}"" is invalid'.format(entry_name))

    if with_sequence:
        return db_dict, seq_dict
    else:
        return db_dict

def get_filepointer(filename):
	"""
	Returns a filepointer to a file based on file name (.gz or - for stdin).
	"""

	fp = None
	if   filename.endswith('.gz'): fp = gzip.open(filename, 'rt')
	elif filename == '-':          fp = sys.stdin
	else:                          fp = open(filename)
	return fp

def read_fasta(filename):
	"""
	Simple fasta reader that returns name, seq for a filename.

	Parameters
	----------
	+ filename
	"""

	name = None
	seqs = []

	fp = get_filepointer(filename)

	while True:
		line = fp.readline()
		if line == '': break
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()


parser = argparse.ArgumentParser(description = "plotting utility for patteRNA")

parser.add_argument("weeksposteriors", metavar = '<file>', type = str,
    help = "posteriors for weeks set")
parser.add_argument("--rev", action = 'store_true',
    help = 'calculate opposite case probabilities (1 -p), for use with posteriors')
parser.add_argument("--save", action = 'store_true',
    help = "save figures instead of displaying them")
parser.add_argument("--dotfile", required=True, metavar='<file>', type = str ,
    help = 'dot file')
parser.add_argument("--numplots", required=False, metavar='<count>', type = int,
    default = 5, help = "Number of plots to plot. -1 plots all. Default: [%(default)s]")

subparser = parser.add_subparsers(help = "save figures instead of displaying")

parser_save = subparser.add_parser("--save")

parser_save.add_argument("path", metavar = '<path>', type = str,
    help = "path to save figure to")


args = parser.parse_args()

dbs, seqs = read_dot_bracket(args.dotfile)

masterlist = {}

for (name,seq) in read_fasta(args.weeksposteriors):
    if name not in dbs:
        print("Error: Unmatched sequence")
        print(name)
        continue

    masterlist[name] = {}
    masterlist[name]['db'] = dbs[name]
    masterlist[name]['seq'] = seqs[name]
    masterlist[name]['posts'] = seq

for name in masterlist:
    print(masterlist[name])


"""
fig, axs = plt.subplots(2,1)
axs[0].plot(names, values)
axs[0].set_ylabel('Pairing Prob')
axs[0].set_xlabel('Position')
axs[0].set_title('Posterior Pairing Probabilities')
axs[0].xaxis.set_major_locator(ticker.MultipleLocator(10))
axs[0].xaxis.set_minor_locator(ticker.MultipleLocator(5))

axs[1].plot(hdslnames, hdslvalues)
axs[1].set_ylabel('Score')
axs[1].set_xlabel('Position')
axs[1].set_title('HDSL Output')
axs[1].xaxis.set_major_locator(ticker.MultipleLocator(10))
axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(5))
loc = ticker.MultipleLocator(base=0.10)
axs[1].yaxis.set_major_locator(loc)
plt.show()
"""
