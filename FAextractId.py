#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bio import SeqIO

def FAextractId(sequence, id_seq, output_fasta):
    """Well filter (include) some ids from a multifasta file
    """
    fasta_seq = SeqIO.parse(sequence, 'fasta')
    buffer_seqs = []
    for record in fasta_seq:
        if record.id == id_seq:
            buffer_seqs.append(record)
            if output_fasta:
                SeqIO.write(buffer_seqs, output_fasta, "fasta")
            else:
                print ">" + record.description
                print record.seq
            return False

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-s", "--sequence", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-i", "--id", help="Id to extract", required=True)
    parser.add_argument("-o", "--output", help="Output file name (.fasta format)",action='store_true')
    args = parser.parse_args()#pylint: disable=invalid-name
    FAextractId(args.sequence, args.id, args.output)
