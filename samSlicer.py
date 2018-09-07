#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import pysam

def samSlicer(sam, id, start, end, move, output):
    """Extract fasta files from annotations
    """
    insam = pysam.AlignmentFile(sam, "r")
    outsam = pysam.AlignmentFile(output, "w", header=insam.header)
    if start and end:
        itersam = insam.fetch(id, start, end)
        for x in itersam:
            if move:
                x.reference_start -= start
                x.next_reference_start -= start
            outsam.write(x)
    else:
        #only by id
        itersam = insam.fetch(id)
        for x in itersam:
            outsam.write(x)
    insam.close()
    outsam.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-a", "--sam", help="SAM file (.sam format)", required=True)
    parser.add_argument("-o", "--output", help="Output file (.fasta)",required=True)
    parser.add_argument("-m", "--move_position", help="Start and end position will be moved -start",action='store_true')
    parser.add_argument("-i", "--sequence_id", help="BAM file")
    parser.add_argument("-s", "--start", help="Start position (empty for start of seq)", action='store_true')
    parser.add_argument("-e", "--end", help="End position (empty for end of seq)", action='store_true')
    args = parser.parse_args()#pylint: disable=invalid-name
    samSlicer(args.sam, args.sequence_id, args.start, args.end, args.move_position, args.output)
