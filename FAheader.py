#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

def FAheader(sequence, output):
    """
    """
    fasta_seq = SeqIO.parse(sequence, 'fasta')
    #TODO if empty seq 
    if not output is None:
        m_file = open(output,'w')
        m_file.close()
    m_file = open(output,'a')
    for record in fasta_seq:
        if output is None:
            print record.id
        else:
            m_file.write(record.id + "\n")
            

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-f", "--fasta_sequence", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-o", "--output", help="Output file (.fasta)", default=None)
    args = parser.parse_args()#pylint: disable=invalid-name
    FAheader(args.fasta_sequence, args.output)
