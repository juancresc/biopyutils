#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

def extractGeneSeq(gff, fasta, genes, output_fasta):
    """Extract fasta files from annotations
    """
    df_gff = pd.read_csv(gff, index_col=False, sep='\t', header=None)
    df_gff.columns = ['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute']
    fasta_seq = SeqIO.parse(fasta, 'fasta')
    buffer_seqs = []
    cont = 0
    gene_positions = {}
    for gene in genes:
        df_extract = df_gff[(df_gff.attribute.str.contains("ID=" + gene)) & (df_gff.feature == "gene")].reset_index(drop=True)
        if(len(df_extract.index) > 0) == 0:
            continue
        newgene = (df_extract.iloc[0].seqname, df_extract.iloc[0].start, df_extract.iloc[0].end, df_extract.iloc[0].strand)
        gene_positions[gene] = (newgene)
    for record in fasta_seq:
        for gene,val in gene_positions.iteritems():
            seq, start, end, strand = val
            if record.id == seq:
                clean_seq = ''.join(str(record.seq).splitlines())
                new_seq = clean_seq[start:end]
                desc = "id:" + str(record.id)
                desc += " start:" + str(start)
                desc += " end:" + str(end)
                desc += " strand:" + str(strand)
                seq = SeqRecord(Seq(new_seq), id=gene, description=desc)
                buffer_seqs.append(seq)
    if output_fasta:
        SeqIO.write(buffer_seqs, output_fasta, "fasta")
    else:
        for bs in buffer_seqs:
            print(">%s %s\n" % (bs.id , bs.description))
            print(bs.seq)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-a", "--annotation", help="Annotation file (.gff3 format)", required=True)
    parser.add_argument("-s", "--sequence", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-g", "--genes", nargs='+', help="Gene list separated by space", required=True)
    parser.add_argument("-o", "--output", help="Output file name (.fasta format)")
    args = parser.parse_args()#pylint: disable=invalid-name
    extractGeneSeq(args.annotation, args.sequence, args.genes, args.output)
