# -*- coding: utf-8 -*-
import pandas as pd
import argparse
import pandasql as pdsql
import timeit

'''
All elements from gff that are partially overlaped with a target element of blat
'''
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--blatoutput", help="BLAT csv output", required=True)
parser.add_argument("-g", "--gff", help="gff file", required=True)
parser.add_argument("-f", "--feature", help="gff feature")
parser.add_argument("-o", "--output", help="Output file in .fasta format", required=True)
args = parser.parse_args()

df_blat = pd.read_csv(args.blatoutput, sep="\t")#, header=None) 
#df_blat.columns = ['match','mismatch','repmatch','ns','qGapCount','qGapBases','tGapCount','tGapBases','strand','qName','qSize','qStart','qEnd','tName','tSize','tStart','tEnd','blockCount','blockSizes','qStarts','tStarts','Qcov','identity']

df_gff = pd.read_csv(args.gff, sep="\t", header=None) 
df_gff.columns = ['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute']
if args.feature:
    df_gff = df_gff[df_gff.feature == args.feature]
pysql = lambda q: pdsql.sqldf(q, globals())
sub_blat = {}
count = 0
new_rows = []
for k,v in df_gff.iterrows():
    if not v.seqname in sub_blat:
        sql = "SELECT * FROM df_blat WHERE tName = '%s'" % (v.seqname,)
        sub_blat[v.seqname] = pysql(sql)
    current = sub_blat[v.seqname]
    sql = """
        SELECT 
            * 
        FROM 
            current 
        WHERE 
            (tStart >= {0} AND tStart <= {1}) OR
            (tEnd >= {0} AND tEnd <= {1})""".format(v.start,v.end)
    res = pysql(sql)
    if len(res.index) > 0:
        new_rows.append(v)
        print count
        count += 1
df_new = pd.DataFrame(new_rows, columns=df_gff.columns).reset_index()
df_new.to_csv(args.output, sep="\t", index=None)
