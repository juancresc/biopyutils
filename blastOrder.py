
def blastOrder(input_file, output):
    import pandas as pd
    df_blast = pd.read_csv(input_file, index_col=False, sep='\t')
    df_blast.columns = ['qseqid','sseqid','pident','length','mismatch','gapopen','qstart','qend','sstart','send','evalue','bitscore']
    df_blast = df_blast.sort_values(['sseqid', 'sstart'])
    df_blast.to_csv(output, sep="\t", index=None)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-i", "--input", help="Input file (.csv format tab-delimited)", required=True)
    parser.add_argument("-o", "--output", help="Output file in .fasta format", required=True)
    args = parser.parse_args()#pylint: disable=invalid-name
    blastOrder(args.input, args.output)
