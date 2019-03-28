#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
This will only work in IWGSC wheat genome assembly annotation (2018)
'''
def gffIntronAdder(annotation, output):
    import pandas as pd
    df = pd.read_csv(annotation, index_col=False, sep='\t', header=None, comment="#")
    df.columns = ['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute']
    result = []
    has_prev_exon = False
    intron_count = 1
    for k, element in df.iterrows():
        if element.feature == 'exon':
            if has_prev_exon:
                prev_transcript_name = prev_exon.attribute.split("Parent=transcript:")[1].split(";")[0]
                transcript_name = element.attribute.split("Parent=transcript:")[1].split(";")[0]
                if prev_transcript_name == transcript_name:
                    intron = []
                    intron.append(element.seqname)
                    intron.append(element.source)
                    intron.append("intron")
                    intron.append(int(prev_exon.end) + 1)
                    intron.append(int(element.start) - 1)
                    intron.append(0)
                    intron.append(element.strand)
                    intron.append(element.frame)
                    intron.append("Parent=transcript:%s;Name=%s-I%i" % (transcript_name, transcript_name, intron_count))
                    result.append(intron)
                    intron_count += 1
            prev_exon = element
            has_prev_exon = True
        result.append(element.tolist())
    df_introns = pd.DataFrame(result)
    df_introns.to_csv(output,sep='\t', encoding='utf-8', index=False, header=False)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-a", "--annotation", help="Annotation file (.gff3 format)", required=True)
    parser.add_argument("-o", "--output", help="Output file (.fasta)", default=None)
    args = parser.parse_args()#pylint: disable=invalid-name
    gffIntronAdder(args.annotation, args.output)
