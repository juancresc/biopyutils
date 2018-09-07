#!/usr/bin/env python
# -*- coding: utf-8 -*-

def AlignPipeline(sam, pad, gff, fasta, output):
    import pandas as pd
    cols = ["QNAME","FLAG","RNAME","POS","MAPQ","CIGAR","MRNM","MPOS","ISIZE","SEQQuery","QUAL"]
    df_sam = pd.read_csv(sam,sep='\t',comment='@', names=cols)
    print(df_sam.head(2))
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-s", "--sam", help="SAM file (.sam)", required=True)
    parser.add_argument("-p", "--pad", help="Pad to join between alignments in nt", default=100)
    parser.add_argument("-g", "--gff", help="Annotation file (.gff)",required=True)
    parser.add_argument("-f", "--fasta", help="Reference genome (.fasta)", required=True)
    parser.add_argument("-o", "--output", help="Output file",required=True)
    args = parser.parse_args()#pylint: disable=invalid-name
    AlignPipeline(args.sam, args.pad, args.gff, args.fasta, args.output)
