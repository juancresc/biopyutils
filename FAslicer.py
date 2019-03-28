#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

def FAslicer(sequence, id, start, end, output = False, keep_id = False):
    """
    """
    fasta_seq = SeqIO.parse(sequence, 'fasta')
    buff = []
    #TODO if empty seq 
    for record in fasta_seq:
        if id is None or record.id == id:
            clean_seq = ''.join(str(record.seq).splitlines())
            if start or end:
                if start is None:
                    start = 0
                if end is None:
                    end = len(clean_seq)
                new_seq = clean_seq[start:end]
                if keep_id:
                    new_id = record.id
                else:
                    new_id = record.id + "_" + str(start) + "_" + str(end)
            else:
                #only by id
                new_seq = clean_seq
                new_id = record.id
            seq = SeqRecord(Seq(new_seq), id=new_id ,description = "_")
            buff.append(seq)
            break
    if not output:
        print('>'+new_id)
        print(new_seq)
        return buff[0]
    else:
        SeqIO.write(buff, output, "fasta")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-f", "--fasta_sequence", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-k", "--keep_id", help="Keep original fasta id", default=False)
    parser.add_argument("-o", "--output", help="Output file (.fasta)", default=False)
    parser.add_argument("-i", "--sequence_id", help="Sequence name id (empty for sinlge seq files)")
    parser.add_argument("-s", "--start", help="Start position (empty for start of seq)",type=int, default=None)
    parser.add_argument("-e", "--end", help="End position (empty for end of seq)", type=int, default=None)
    args = parser.parse_args()#pylint: disable=invalid-name
    FAslicer(args.fasta_sequence, args.sequence_id, args.start, args.end, args.output, args.keep_id)
