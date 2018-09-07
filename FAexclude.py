#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bio import SeqIO

def exclude(sequence, records, output_fasta):
    """Well exclude some ids from a multifasta file
    """
    fasta_seq = SeqIO.parse(sequence, 'fasta')
    buffer_seqs = []
    for record in fasta_seq:
        if record.id in records:
            continue
        buffer_seqs.append(record)
    SeqIO.write(buffer_seqs, output_fasta, "fasta")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-s", "--sequence", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-e", "--exclude", help="Exclude some ids", action='append')
    parser.add_argument("-o", "--output", help="Output file name (.fasta format)", required=True)
    args = parser.parse_args()#pylint: disable=invalid-name
    exclude(args.sequence, args.exclude, args.output)
