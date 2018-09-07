#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Gets a .gff3 file which contains exons and create introns as an output .gff3
Juan Manuel Crescente
29 May 2018
INTA / CONICET
'''
def gffIntronMaker(annotation, output):
    """
    Not implemented yet
    """
    import pandas as pd
    df = pd.read_csv(annotation, index_col=False, sep='\t', header=None)    
    df.columns = ['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute']
    df = df[(df.feature == 'exon')]
    df_introns.to_csv(output,sep='\t', encoding='utf-8', index=False, header=False, quoting=csv.QUOTE_NONE)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-a", "--annotation", help="Annotation file (.gff3 format)", required=True)
    parser.add_argument("-o", "--output", help="Output file (.fasta)", default=None)
    args = parser.parse_args()#pylint: disable=invalid-name
    gffIntronMaker(args.annotation, args.output)
