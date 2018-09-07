import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--blastoutput", help="BLAT csv output", required=True)
parser.add_argument("-c", "--minPindent", help="Filter by this value", type=int)
parser.add_argument("-o", "--output", help="Output file in .fasta format", required=True)
args = parser.parse_args()

#get the best blast hit 
df = pd.read_csv(args.blastoutput,sep="\t", header=None) 
df.columns = ['qseqid','sseqid','pident','length','mismatch','gapopen','qstart','qend','sstart','send','evalue','bitscore']
df = df[df['pident']>= args.minPindent]
df.to_csv(args.output, sep="\t", index=None)
