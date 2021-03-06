#!/usr/bin/env python3

"""Aligns sequences"""

__author__ = 'Luke Swaby (lds20@ic.ac.uk), ' \
             'Jinkai Sun (jingkai.sun20@imperial.ac.uk), ' \
             'Acacia Tang (t.tang20@imperial.ac.uk), ' \
             'Dengku Tang (dengkui.tang20@imperial.ac.uk)'
__version__ = '0.0.1'

## Imports ##

import sys

## Functions ##

def calculate_score(s1, s2, l2, startpoint):
    """Calculate best alignment score (no. of matched bases) of 2 padded
     sequences

     Arguments:
     - s1 (str) : sequence string 1
     - s2 (str) : inital consumer density
     - startpoint (int) : index of where to begin alignment

    Output:
     - Integer representing number of matched bases
    """
    score = 0
    for i in range(l2):
        if s1[i + startpoint] == s2[i]:
            score += 1
        else:
            continue

    return score

def extract_seq(filename):
    """Extract seq from file (and header if present)

    Arguments:
     - filename (str) : path to file containing sequence

    Output:
     - seq (str) : sequence string
     - head (str) : header string (or None if absent)
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

def main(argv):
    """Align sequences and write alignment to fasta file, printing score
    achieved to the command line.
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
        s1 = (l2 - 1) * "-" + seq1 + (l2 - 1) * "-"
        s2 = seq2 + (l1 + l2 - 2) * '-'
        h1 = head1
        h2 = head2
    else:
        s1 = (l1 - 1) * "-" + seq2 + (l1 - 1) * "-"
        s2 = seq1 + (l1 + l2 - 2) * '-'
        l1, l2 = l2, l1
        h1 = head2
        h2 = head1

    # Find the best match (highest score) for the two sequences
    scores = {}
    my_best_score = -1

    for i in range(l1 + l2 - 1):  # Note that you just take the last alignment with the highest score
        z = calculate_score(s1, s2, l2, i)
        if z >= my_best_score:
            my_best_score = z
            scores[i] = my_best_score

    aligns = ["-" * i + s2[:-i] for i in scores.keys() if
              scores[i] == max(scores.values())]


    # Clip trailing hyphens (by determining start/stop values)
    start = min(aln.find(next(filter(str.isalpha, aln))) for aln in aligns + [s1])

    reverse = [s[::-1] for s in aligns + [s1]]
    stop = min(aln.find(next(filter(str.isalpha, aln))) for aln in reverse)

    s1 = s1[start:-stop]

    # Write output
    with open('../Results/align_seqs_better.fa', 'w') as out:
        for no, algmt in enumerate(aligns, 1):
            if h2:
                # print s2 header if present
                out.write(f'{h2} — Alignment {no}; Score: {my_best_score}\n')
            out.write(f'{algmt[start:-stop]}\n')
        if h1:
            # print s1 header if present
            out.write(f'{h1}\n')
        out.write(s1)

    print(f'Best Score: {my_best_score}')

    return 0

if __name__ == '__main__':
    status = main(sys.argv)
    sys.exit(status)
