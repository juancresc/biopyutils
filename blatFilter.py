import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--blatoutput", help="BLAT csv output", required=True)
parser.add_argument("-c", "--minCoverage", help="Output file in .fasta format", type=int)
parser.add_argument("-d", "--minIdentity", help="Output file in .fasta format", type=int)
parser.add_argument("-o", "--output", help="Output file in .fasta format", required=True)
args = parser.parse_args()

#get the best blast hit 
df = pd.read_csv(args.blatoutput,sep="\t", header=None) 
df.columns = ['match','mismatch','repmatch','ns','qGapCount','qGapBases','tGapCount','tGapBases','strand','qName','qSize','qStart','qEnd','tName','tSize','tStart','tEnd','blockCount','blockSizes','qStarts','tStarts']
df['Qcov'] = (df['qEnd'] - df['qStart']) * 100 / df['qSize']
df['identity'] = (df['match'] * 100) /  (df['qEnd'] - df['qStart'])
if args.minCoverage:
    df = df[df['Qcov']>= args.minCoverage]
if args.minIdentity:
    df = df[df['identity']>= args.minIdentity]
df = df.sort_values(['tName', 'tStart'])
df.to_csv(args.output, sep="\t", index=None)
