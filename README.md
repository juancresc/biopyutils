## bioinformatics tools written in python for managing .fasta, .gff, BLAST results 

## FAshuff.py
Divide a genome in k-mers, shuffle and save the output.

python FAshuff.py -i genome.fasta -o shuffled.fasta -k 6



## FAexclude.py

- -s --sequence
- -e --exclude
- -o --output

takes _sequence_ and exclude _exclude_ ids from the multifasta file. Saves the resulting .fasta in _output_


# GFF3 files

Before using any gff parsing with pandas, headers should be removed. 


cat ann.gff |  sed '/^#/ d' > ann-clean.gff
