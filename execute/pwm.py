
import math
import sys

def make_pwm(seqs):
	"""
	Function for making position weight matrix

	**Parameters:**

	+ seqs -- list of sequences (list)

	**Returns:**

	+ list of dictionaries containing nucleotide frequencies

	"""

	length = len(seqs[0])

	# create counts
	count = []
	for i in range(length): count.append({'A':0, 'C':0, 'G':0, 'T':0})
	total = 0
	for i in range(len(seqs)):
		seq = seqs[i]
		total += 1
		for i in range(len(seq)):
			count[i][seq[i]] += 1

	# create freqs
	freq = []
	for i in range(length): freq.append({})
	for i in range(length):
		for c in count[i]:
			freq[i][c] = count[i][c] / total

	return freq

def score_pwm(pwm, seq):
	"""
	*Function to show scoring against the created position weight matrix* <br/>

	*Returns a score for the sequence scored against pwm* <br/>

	**Parameters:**
	_______________
	+ pwm -- position weight matrix (list of dictionaries) <br/>
	  	** for help refer to make_pwm function
	+ seq -- a single sequence (int)
  	"""
	p = 1 #this is the baseline score
	for i in range(len(seq)): #for each bp in the query sequence...
		p *= pwm[i][seq[i]] #your score is multiplied by the frequency of that base at that same position in the array
	return p #the score is returned

def display_pwm(pwm):
	"""
  	*Function that displays the probability of each nucleotide in a given position of the pwm* <br/>

	*Returns a pwm in a readable format* <br/>

	**Parameters:**
	_______________
  	+ pwm -- position weight matrix (list of dictionaries) <br/>
  		** for help refer to make_pwm function
  	"""

	for i in range(len(pwm)):
		print(f'{str(i)}\t{pwm[i]["A"]:.3f}\t{pwm[i]["C"]:.3f}\t{pwm[i]["G"]:.3f}\t{pwm[i]["T"]:.3f}')


def threshold(scores, prandom): #this takes a list of scores and their labels, and determines a threshold via binary sort
	length = len(scores) #determine length of the list scores
	middlei = round((length - 1)/2)
	#print(middlei, scores[middlei][1], prandom) #determine the middle index. Rounding up or down shouldn't matter here.
	if prandom == scores[middlei][1] or middlei == 0: #we have a match, or its all good?! This is our threshold
		return prandom
	else:
		if prandom < scores[middlei][1]: #our threshold is in the bottom half
			scores = scores[0:middlei] #sets the old middlei to our new upper bound
			return prandom
		else:#our threshold is in the top half
			scores = scores[middlei:length] #makes middlei the first index
			prandom = threshold(scores, prandom) #recursive call to same function
			return prandom

def entropy(pwm):
	"""
	*Function that shows how the randomness of the chosen base in a given position* <br/>

  	*Returns an entropy score (float)* <br/>

	**Parameters:**
	_______________

	+ pwm -- posiiton weight matrix (list of dictionaries) <br/>
  		** for help refer to make_pwm function
  	"""

	H = 0

	for i in range(len(pwm)):
		h = 0
		for nt in pwm[i]:
			if pwm[i][nt] != 0: h += pwm[i][nt] * math.log2(pwm[i][nt])
		H += 2 + h

	return H
