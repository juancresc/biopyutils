import sys
from Bio import SeqIO

def human(size):
    step_to_greater_unit = 1000.
    number_of_bytes = float(size)
    unit = 'bp'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'Kbp'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'Mbp'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'Gbp'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'Tbp'

    precision = 1
    number_of_bytes = round(number_of_bytes, precision)
    return str(number_of_bytes) + unit

FastaFile = open(sys.argv[1], 'rU')
total = 0
for rec in SeqIO.parse(FastaFile, 'fasta'):
    name = rec.id
    seq = rec.seq
    seqLen = len(rec)
    total += seqLen
    print name, seqLen, human(seqLen)
print "Total", total, human(total)
FastaFile.close()

