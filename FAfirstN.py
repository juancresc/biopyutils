#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bio import SeqIO

def FAfirstN(sequence, n, output_fasta):
    """Well filter (include) some ids from a multifasta file
    """
    fasta_seq = SeqIO.parse(sequence, 'fasta')
    buffer_seqs = []
    count = 0
    for record in fasta_seq:
        if count == n:
            break
        count += 1
        print(count, n)
        buffer_seqs.append(record)
    if output_fasta:
        SeqIO.write(buffer_seqs, output_fasta, "fasta")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-s", "--sequence", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-n", "--n", help="First n sequences", type=int)
    parser.add_argument("-o", "--output", help="Output file name (.fasta format)", default=False)
    args = parser.parse_args()#pylint: disable=invalid-name
    FAfirstN(args.sequence, args.n, args.output)
