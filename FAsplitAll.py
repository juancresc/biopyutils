#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bio import SeqIO

def FASplitAll(sequence, outdir):
    """Well exclude some ids from a multifasta file
    """
    if outdir[-1] != "/":
        outdir += "/"
    fasta_seq = SeqIO.parse(sequence, 'fasta')
    for record in fasta_seq:
        SeqIO.write(record, outdir + record.id + ".fasta", "fasta")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-s", "--sequence", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-o", "--outdir", help="Output directory", default='')
    args = parser.parse_args()#pylint: disable=invalid-name
    FASplitAll(args.sequence, args.outdir)
