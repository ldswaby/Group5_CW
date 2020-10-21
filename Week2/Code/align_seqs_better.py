#!/usr/bin/env python3

"""Aligns sequences"""

__author__ = 'Luke Swaby (lds20@ic.ac.uk), ' \
             'Jinkai Sun (jingkai.sun20@imperial.ac.uk), ' \
             'Acacia Tang (t.tang20@imperial.ac.uk), ' \
             'Dengku Tang (dengkui.tang20@imperial.ac.uk)'
__version__ = '0.0.1'

## Imports ##
import sys, re

## Functions ##
def calculate_score(s1, s2, l1, l2, startpoint):
    """Calculate best alignment score (no. of matched bases) of 2
    sequences
    """
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched += "*"
                score += 1
            else:
                matched += "-"

    return score

def extract_seq(filename):
    """Extract seq from file (and header if present)
    """
    with open(filename) as f:
        line1 = f.readline().strip()
        header = line1.startswith('>')
        if header:
            # If there a header...
            head = line1
            seq = ''.join(line.strip() for line in f)
        else:
            # If there is no header (just seq)...
            f.seek(0)  # Return to first line
            head = None
            seq = ''.join(line.strip() for line in f)  # Join all lines into seq var

    return seq, head

#TODO: wouldn't it make more sense to have this as argv[1:]? Otherwise if
# someone wants to import it as a module and use main() they'd have to input
# a random first element of the list (as 'align_seqs_better.py' is no longer there)
def main(argv):
    """Run functions
    """
    # Parse inputs
    if len(argv) == 1:
        seqfile1 = '../Data/407228326.fasta'
        seqfile2 = '../Data/407228412.fasta'
    elif len(argv) == 2:
        sys.exit(
            'ERROR: this script takes 2 input seq files. You have provided 1.')
    elif len(argv) == 3:
        seqfile1 = argv[1]
        seqfile2 = argv[2]
    else:
        sys.exit('ERROR: too many arguments were provided.')

    ## TEXT IN
    seq1, head1 = extract_seq(seqfile1)
    seq2, head2 = extract_seq(seqfile2)

    # Assign the longer sequence s1, and the shorter to s2
    # l1 is length of the longest, l2 that of the shortest

    l1 = len(seq1)
    l2 = len(seq2)
    if l1 >= l2:
        s1 = seq1
        h1 = head1
        s2 = seq2
        h2 = head2
    else:
        s1 = seq2
        h1 = head2
        s2 = seq1
        h2 = head1
        l1, l2 = l2, l1  # swap the two lengths

    # Find the best match (highest score) for the two sequences
    aligns = {}
    #TODO: More memory-efficient way of doing this^?
    my_best_score = -1

    for i in range(l1):
        # Find highest score
        z = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:
            my_best_score = z
        # Load dict with scores for keys and lists of corresponding alignments
        # for values.
        if z in aligns.keys():
            aligns[z].append("-" * i + s2)
        else:
            aligns[z] = ["-" * i + s2]

    # Write output
    with open('../Results/group_better_algmt.fa', 'w') as out:
        # TODO: Reconsider these^ names?
        for no, algmt in enumerate(aligns[my_best_score], 1):
            if h2:
                # print s2 header if present
                out.write(f'{h2} — Alignment {no}; Score: {my_best_score}\n')
            out.write(f'{algmt}\n')
        if h1:
            # print s1 header if present
            out.write(f'{h1}\n')
        out.write(s1)
        #out.write('\n\n' + f"Best score: {my_best_score}")

    return 0

if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)