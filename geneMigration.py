#!/usr/bin/env python
# -*- coding: utf-8 -*-

def geneMigration(gene_name, annotation_1, sequence_1, annotation_2, sequence_2, output):
    """
    Given a gene name will search it in annotation_1, extract
    fasta from sequence_1 and search its results in sequence_2,
    search for the corresponding annotation in annotation_2
    and return the gene name.

    It will translate a gene from a refseq to a newer version
    """
    import os
    from geneGFF2FA import geneGFF2FA
    from subprocess import Popen, PIPE
    from gffSearch import gffSearch

    query_filename = 'trash/query.fa'
    geneGFF2FA(gene_name, annotation_1, sequence_1, query_filename)
    cmd_list = [
    'blastn',
    '-query',query_filename,
    '-subject',sequence_2,
    '-max_target_seqs','1',
    '-evalue','10e-3',
    '-strand','plus',
    '-outfmt','6']
    p = Popen(cmd_list, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()#os.remove(query_filename)
    lines = out.splitlines()
    for row in lines:
        row = row.split()
        sseqid = int(row[2])
        sstart = int(row[9])
        send = int(row[10])
        print(sseqid, sstart, send)
        results = gffSearch(annotation_2, sseqid, sstart, send)
        for k,v in results.iterrows():
            print(v)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-g", "--gene_name", help="Gene name", required=True)
    parser.add_argument("-a1", "--annotation_1", help="Annotation file 1 (.gff3 format)", required=True)
    parser.add_argument("-s1", "--sequence_1", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-a2", "--annotation_2", help="Annotation file 2 (.gff3 format)", required=True)
    parser.add_argument("-s2", "--sequence_2", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-o", "--output", help="Output file name (.fasta format)")
    args = parser.parse_args()#pylint: disable=invalid-name
    geneMigration(args.gene_name, args.annotation_1, args.sequence_1, args.annotation_2, args.sequence_2, args.output)


#python geneMigration.py -g TRIAE_CS42_2BL_TGACv1_129652_AA0391760 -a1 /media/crescentejuan/Data/TGAC/Triticum_aestivum.TGACv1.39.gff3 -s1 /media/crescentejuan/Data/TGAC/Triticum_aestivum.TGACv1.dna.toplevel.fa -a2 /media/crescentejuan/Data/IWGSC/iwgsc_refseqv1.0_HighConf_2017Mar13.gff3 -s2 /media/crescentejuan/Data/iwgsc_refseqv1.0_all_chromosomes/161010_Chinese_Spring_v1.0_pseudomolecules.fasta