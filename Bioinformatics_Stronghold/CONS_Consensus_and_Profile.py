#!/usr/bin/env python3

### CONS: Consensus and Profile

### Given: A collection of at most 10 DNA strings of equal
### length (at most 1kbp) in FASTA format

### Return: A consensus string and profile matrix for the
### collection. (If several possible consensus strings exist,
### then you may return any one of them).

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

### Make a dictionary containing the number of each
### nucleotide at each position
countA = []
countT = []
countG = []
countC = []
cons = []
i = 0
while i < len(sequence[0]):
    pos = []
    k = 0
    while k < len(ID):
        pos.append(sequence[k][i])
        k = k + 1
    i = i + 1
    A = pos.count('A')
    T = pos.count('T')
    G = pos.count('G')
    C = pos.count('C')
    countA.append(A)
    countT.append(T)
    countG.append(G)
    countC.append(C)
    if A == max(A,T,G,C):
        cons.append("A")
    elif T == max(A,T,G,C):
        cons.append("T")
    elif C == max(A,T,G,C):
        cons.append("C")
    else:
        cons.append("G")

profile = {"A": countA, "C": countC, "G": countG, "T": countT}

### Present the results

for nu in cons:
    print(nu, end = "")
print("\n")

for key in profile.keys():
    print(key, end = "")
    print(":", end = " ")
    for value in profile[key]:
        print(value, end = " ")
    print("\n")
