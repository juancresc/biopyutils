#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

def geneGFF2FA(gene, annotation, sequence , output):
    """Extract fasta files from annotations
    """
    df_gff = pd.read_csv(annotation, index_col=False, sep='\t', header=None)
    df_gff.columns = ['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute']
    fasta_seq = SeqIO.parse(sequence, 'fasta')
    buffer_seqs = []
    cont = 0
    df_extract = df_gff[(df_gff.attribute.str.contains('ID='+gene)) & (df_gff.feature=='gene')]
    gene_gff = df_extract.iloc[0]
    for record in fasta_seq:
        if record.id != gene_gff.seqname:
            continue
        clean_seq = ''.join(str(record.seq).splitlines())
        if int(gene_gff.start) < 0:
            start = 0
        else:
            start = int(gene_gff.start)
        if int(gene_gff.end) > len(clean_seq):
            end = len(clean_seq)
        else:
            end = int(gene_gff.end)
        new_seq = clean_seq[start:end]
        att = gene_gff.attribute
        desc = "seq:" + str(record.id)
        desc += " start:" + str(gene_gff.start)
        desc += " end:" + str(gene_gff.end)
        desc += " strand:" + str(gene_gff.strand)
        seq = SeqRecord(Seq(new_seq), id=gene, description=desc)
        if not output:
            return seq
        else:
            buffer_seqs.append(seq)
        break
    if output:
        SeqIO.write(buffer_seqs, output, "fasta")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-g", "--gene", help="Annotation file (.gff3 format)", required=True)
    parser.add_argument("-a", "--annotation", help="Annotation file (.gff3 format)", required=True)
    parser.add_argument("-s", "--sequence", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-o", "--output", help="Output file name (.fasta format)")
    args = parser.parse_args()#pylint: disable=invalid-name
    geneGFF2FA(args.gene, args.annotation, args.sequence, args.output)
