#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

def FAslicer(sequence, id, start):
    """
    """
    fasta_seq = SeqIO.parse(sequence, 'fasta')
    buff = []
    #TODO if empty seq 
    for record in fasta_seq:
        if id is None or record.id == id:
            clean_seq = ''.join(str(record.seq).splitlines())
            return clean_seq[start:start+1]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-f", "--fasta_sequence", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-i", "--sequence_id", help="Sequence name id (empty for sinlge seq files)")
    parser.add_argument("-p", "--position", help="Start position (empty for start of seq)",type=int, required=True)
    args = parser.parse_args()#pylint: disable=invalid-name
    print(FAslicer(args.fasta_sequence, args.sequence_id, args.start))
