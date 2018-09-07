#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bio import SeqIO

def FAstats(sequence):
    """
    """
    fasta_seq = SeqIO.parse(sequence, 'fasta')
    buffer_seqs = []
    total_len = 0
    count = 0
    for record in fasta_seq:
        print("%s %i" % (record.id, len(record)))
        total_len += len(record)
        count += 1
    print "avg len %i" % ( total_len / count, )
    print "total seqs %i" % ( count, )
    print "total length %i" % ( total_len, )
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-s", "--sequence", help="Sequence file (.fasta)", required=True)
    args = parser.parse_args()#pylint: disable=invalid-name
    FAstats(args.sequence)
