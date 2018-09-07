import pandas as pd

def blast1hit(allhits, output):
    '''
    Needs documentation
    '''
    df = pd.read_csv(allhits,sep="\t", header=None)
    df.columns = ['qseqid','sseqid','pident','length','mismatch','gapopen','qstart','qend','sstart','send','evalue','bitscore']
    if output:
        df.groupby('qseqid').head(1).to_csv(output, sep="\t", index=None)
    else:
        return df.groupby('qseqid').head(1)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-a", "--allhits", help="Allhits file (.csv format tab-delimited)", required=True)
    parser.add_argument("-o", "--output", help="Output file in .fasta format", )
    args = parser.parse_args()#pylint: disable=invalid-name
    blast1hit(args.allhits, args.output)
