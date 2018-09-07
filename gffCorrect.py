#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gffCorrect(gff, output):
    import pandas as pd
    import numpy as np
    """Extract fasta files from annotations
    """
    df = pd.read_csv(gff, index_col=False, sep='\t', header=None)
    df.columns = ['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute']
    df['start'] = df['start'].astype(int)
    df['end'] = df['end'].astype(int)
    df['strand'] = np.where(df.start < df.end, '+', '-')
    #negatie stand correction
    df['start_2'] = np.where(df.start > df.end, df.end, df.start)
    df['end_2'] = np.where(df.start < df.end, df.end, df.start)
    df['start'] = df['start_2']
    df['end'] = df['end_2']
    df.insert(0, 'new_id', range(0, len(df)))
    df["attribute"] = 'id=' + df["new_id"].map(str) + ';MITE=' + df["attribute"]

    del df['new_id']
    del df['start_2']
    del df['end_2']
    df.to_csv(args.output, sep="\t", header=None, index=None)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-g", "--gff", help=".gff3 format", required=True)
    parser.add_argument("-o", "--output", help="Output file name (.fasta format)")
    args = parser.parse_args()#pylint: disable=invalid-name
    gffCorrect(args.gff, args.output)
