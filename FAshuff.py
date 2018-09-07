
def shuffle(input, k, output):
    from Bio import SeqIO
    from random import shuffle
    from Bio.SeqRecord import SeqRecord
    from Bio.Seq import Seq
    fasta_seq = SeqIO.parse(input, 'fasta')
    total_buff = []
    for record in fasta_seq:
        print 'Shuffling chromosome', record.id
        buff = []
        clean_seq = ''.join(str(record.seq).splitlines())
        for i in range(0,len(clean_seq),k):
            buff.append(clean_seq[i:i+k])
        shuffle(buff)
        fa_seq = ''.join(buff)
        seq = SeqRecord(Seq(fa_seq), id=record.id, description=record.description)
        total_buff.append(seq)
        print 'Done chromosome', record.id
    SeqIO.write(total_buff, output, "fasta")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument("-i", "--input", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-o", "--output", help="Sequence file (.fasta)", required=True)
    parser.add_argument("-k", "--klen", help="k-mer's k",type=int, required=True)
    args = parser.parse_args()#pylint: disable=invalid-name
    shuffle(args.input, args.klen, args.output)