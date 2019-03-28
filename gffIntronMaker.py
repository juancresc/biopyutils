#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This will only work in IWGSC wheat genome assembly annotation (2018)
'''
def gffIntronMaker(annotation, output):
    import pandas as pd
    introns = []
    df = pd.read_csv(annotation, index_col=False, sep='\t', header=None, comment="#")
    df.columns = ['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute']
    df_genes = df[(df.feature == 'mRNA')] # because I need to go transcript by transcript
    for k1, gene in df_genes.iterrows():
        transcript_name = gene.attribute.split("ID=transcript:")[1].split(";")[0]
        #gene_name = gene.attribute.split("Parent=gene:")[1].split(";")[0]
        df_exons = df[(df.feature == 'exon') & (df.attribute.str.contains('Parent=transcript:' + transcript_name))]
        df_exons.reset_index(inplace=True)
        df_exons.sort_values(['start'], inplace=True)
        if len(df_exons.index) <= 1:
            continue
        intron_count = 0
        for k2, exon in df_exons.iloc[:-1].iterrows():
            exon_next = df_exons.loc[[k2 + 1]]
            intron_count += 1
            intron = []
            intron.append(exon.seqname)
            intron.append(exon.source)
            intron.append("intron")
            intron.append(int(exon.end) + 1)
            intron.append(int(exon_next.start) - 1)
            intron.append(0)
            intron.append(exon.strand)
            intron.append(exon.frame)
            intron.append("Parent=transcript:%s;Name=%s-I%i" % (transcript_name, transcript_name, intron_count))
            introns.append(intron)
    df_introns = pd.DataFrame(introns)
    df_introns.to_csv(output,sep='\t', encoding='utf-8', index=False, header=False)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-a", "--annotation", help="Annotation file (.gff3 format)", required=True)
    parser.add_argument("-o", "--output", help="Output file (.fasta)", default=None)
    args = parser.parse_args()#pylint: disable=invalid-name
    gffIntronMaker(args.annotation, args.output)
