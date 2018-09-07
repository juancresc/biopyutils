#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bio import SeqIO

def filter(sequence, records, output_fasta):
    """Well filter (include) some ids from a multifasta file
    """
    fasta_seq = SeqIO.parse(sequence, 'fasta')
    buffer_seqs = []
    for record in fasta_seq:
        if record.id in records:
            #search for the whole id in the records
            buffer_seqs.append(record)
        else:
            #search for partial string matching
            for r in records:
                if r in record.id or r in record.description:
                    buffer_seqs.append(record)
    if output_fasta and output_fasta != "":
        SeqIO.write(buffer_seqs, output_fasta, "fasta")
    else:
        for bs in buffer_seqs:
            print ">" + bs.id + "\n"
            print bs.seq

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-s", "--sequence", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-i", "--include", help="Filter some ids", action='append')
    parser.add_argument("-o", "--output", help="Output file name (.fasta format)")
    args = parser.parse_args()#pylint: disable=invalid-name
    filter(args.sequence, args.include, args.output)
