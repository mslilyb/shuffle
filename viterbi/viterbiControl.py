import math
import seqio
import argparse
import model

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description ='Simple Gene Finder using a Viterbi Algorithm') #reads in user input

  parser.add_argument('--exonFile', required = True, type = str, metavar = '<file>', help = 'fasta file of known exons')
  parser.add_argument('--intronFile', required = True, type = str, metavar = '<file>', help = 'fasta file of known introns')
  parser.add_argument('--queryFile', required = True, type = str, metavar = '<file>', help = 'fasta file of query sequence')
  parser.add_argument('--order', required = False, type = int, default = 1, metavar = '<int>', help = 'desired order of model used (WIP, not yet functional)')

  args = parser.parse_args() #sets our arguments to match user input

  exons = [(name, seq) for name, seq in seqio.read_fasta(args.exonFile)] #reads all the sequences in the exon file and preserves their name
  introns = [(name, seq) for name, seq in seqio.read_fasta(args.intronFile)] #reads all the sequences in the intron file and preserves their name
  query = [(name, seq) for name, seq in seqio.read_fasta(args.queryFile)] #reads all the query sequences and preserves their names

  exonEmissionP = model.findEmissionP(exons)
  intronEmissionP = model.findEmissionP(introns) #these both find the emission probabilities of nucleotides in exons or introns

  exonTransitionP = model.findTransitionP(exons)
  intronTransitionP  = model.findTransitionP(introns)

  for seq in query: #for each sequence in the fasta file, run the algorithm
      viterbi = []
      viterbi[0] = [(0.5, 'exon', 'none'), (0.5, 'intron', 'none')] #initializes the list with the first tuple. Entries are formatted as follows: (probability, current state, previous state)
      previousPos = 0 #where we are tracing from
      currentPos = args.order #how many positions are we making significant for context. default 1

      for nt in seq[1]: #for each nucleotide in each sequence, a list is generated using the viterbi algorithm that gives the exon/intron breakdown
        index = 0
        exonPreviousP = 0 #this is a sum of log probabilities that
        intronPreviousP = 0

          while (previousPos + index) < currentPos: #this while loop is a work in progress implementation of a variable order number model. current issue is just how to incorporate previous probabilities. Is it every permutation? That's my gut feeling
              exonPreviousP += math.log(viterbi[previousPos][0][0]) #sums log probabilities of exon -> exon transitions
              intronPreviousP += math.log(viterbi[previousPos][1][0]) #sums log probabilities of intron -> intron transitions
              index += 1

        exonRemainP = ((exonPreviousP + math.log(exonTransitionP['remain']) + math.log(exonEmissionP[nt])), 'Exon', 0) #these statements construct tuples using the same format as the initial ones
        exonChangeP = ((exonPreviousP + math.log(exonTransitionP['change']) + math.log(exonEmissionP[nt])), 'Exon', 1)
        intronRemainP = ((intronPreviousP + math.log(intronTransitionP['remain']) + math.log(intronEmissionP[nt])), 'Intron', 1)
        intronChangeP = ((intronPreviousP + math.log(intronTransitionP['change']) + math.log(intronEmissionP[nt])), 'Intron', 0)

        viterbi.append([max(exonRemainP, exonChangeP), max(intronRemainP, intronChangeP)]) #adds the maximum probabilities for both states to the list
        currentPos += 1 #iterates the count indices to iterate along the list
        previousPos += 1 #iterates the count indices to iterate along the list

    
