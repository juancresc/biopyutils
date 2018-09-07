#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bio import SeqIO

def FAextractN(sequence, n, output):
    """Well exclude some ids from a multifasta file
    """
    fasta_seq = SeqIO.parse(sequence, 'fasta')
    buffer_seqs =[] 
    for i in range(n):
        record = fasta_seq.next()
        buffer_seqs.append(record)
    SeqIO.write(buffer_seqs, output + ".fasta", "fasta")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-s", "--sequence", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-n", "--number", help="Filter n first sequences", type=int, required=True)
    parser.add_argument("-o", "--output", help="Output file name (.fasta format)", required=True)
    args = parser.parse_args()#pylint: disable=invalid-name
    FAextractN(args.sequence, args.number, args.output)
