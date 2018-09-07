import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--reference_annotation", help="Reference annotation file (.gff3 format)", required=True)
parser.add_argument("-a", "--allhits", help="Allhits file (.csv format tab-delimited)", required=True)
parser.add_argument("-o", "--output", help="Output file in .fasta format", required=True)
parser.add_argument("-d", "--delta", help="Move +- delta nt up and downstream", default=0, type=int)
args = parser.parse_args()

#get the best blast hit 
df = pd.read_csv(args.allhits,sep="\t", header=None)
df.columns = ['qseqid','sseqid','pident','length','mismatch','gapopen','qstart','qend','sstart','send','evalue','bitscore']
df_total = pd.DataFrame()
df_gff = pd.read_csv(args.reference_annotation, index_col=False, sep='\t',header=None)
df_gff.columns = ['seqname' , 'source' , 'feature' , 'start' , 'end' , 'score' , 'strand' , 'frame' , 'attribute']
for index,hit in df.iterrows():
    bp_from = hit.sstart
    bp_to = hit.send
    if bp_from > bp_to:
        bp_aux = bp_from
        bp_from = bp_to
        bp_to = bp_aux
    lenght = int(bp_to) - int(bp_from)
    bp_from -= args.delta
    bp_to += args.delta
    seqid = hit.sseqid
    #extract annotation
    df_res = df_gff[(df_gff.seqname == seqid) & (df_gff.start >= bp_from) & (df_gff.end <= bp_to)]
    df_total.append(df_res,ignore_index=True)
df_total.to_csv(args.output, sep="\t", header=None, index=None)
