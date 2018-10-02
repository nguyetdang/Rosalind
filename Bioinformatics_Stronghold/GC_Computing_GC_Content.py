#!/usr/bin/env python3

### GC: Computing GC Content

### Given: At most 10 DNA strings in FASTA format (of length
### 1 kbp each)

### Return: The ID of the string having the highest GC-content
### followed by the GC-content of that string. Rosalind allows
### for a default error of 0.001 in all decimal answers unless
### otherwise stated; please see the note on absolute errorself.

### Input

from itertools import groupby

def fasta_iter(fasta_name):
    fh = open(fasta_name)
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        headerStr = header.__next__()[1:].strip()
        seq = "".join(s.strip() for s in faiter.__next__())
        yield (headerStr, seq)


path_to_input = input("Input file: ")
fasta = fasta_iter(path_to_input)

ID = []
sequence = []
for ff in fasta:
    headerStr, seq = ff
    ID.append(headerStr)
    sequence.append(seq)

### Calculate GC content for each sequence
GC = []

for seq in sequence:
    GC.append((seq.count("C") + seq.count("G"))*100/len(seq))

maxGC_index = GC.index(max(GC))
print(ID[maxGC_index])
print(GC[maxGC_index])
