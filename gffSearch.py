#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import csv

def gffSearch(annotation, seqid, start, end, output = None):
    '''
    '''
    df_gff = pd.read_csv(annotation, index_col=False, sep='\t', header=None)
    df_gff.columns = ['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute']
    if start and end:
        if start != None and end != None:
            df_extract = df_gff[(df_gff.seqname == seqid) & (df_gff.start >= start) & (df_gff.end <= end)]
        if start != None and end is None:
            df_extract = df_gff[(df_gff.seqname == seqid) & (df_gff.start >= start)]
        if start is None and end != None:
            df_extract = df_gff[(df_gff.seqname == seqid) & (df_gff.end <= end)]
        if start is None and end is None:
            df_extract = df_gff[(df_gff.seqname == seqid)]
    else:
        #only by seqid
        df_extract = df_gff[(df_gff.seqname == seqid)]
    if output is None:
        return df_extract.to_string(output, index=False, header=False)
    else:
        df_extract.to_csv(output,sep='\t', encoding='utf-8',index=False,header=False,quoting=csv.QUOTE_NONE)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-a", "--annotation", help="Annotation file (.gff3 format)", required=True)
    parser.add_argument("-o", "--output", help="Output file (.fasta)", default=None)
    parser.add_argument("-i", "--sequence_id", help="Sequence name id (empty for sinlge seq files)")
    parser.add_argument("-s", "--start", help="Start position (empty for start of seq)", type=int)
    parser.add_argument("-e", "--end", help="End position (empty for end of seq)", type=int)
    args = parser.parse_args()#pylint: disable=invalid-name
    gffSearch(args.annotation, args.sequence_id, args.start, args.end, args.output)
