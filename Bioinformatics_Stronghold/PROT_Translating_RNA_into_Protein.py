#!/usr/bin/env python3

### PROT: Translating RNA into Protein

### Given: An RNA string s corresponding to a strand of mRNA
### (of length at most 10 kbp)

### Return: The protein string encoded by s

### Input

path_to_input = input("Input file: ")
f_input = open(path_to_input, "r")
RNAseq = f_input.readline()
RNAseq = RNAseq.replace("\n","")

### Translate RNA into Protein

def trans_protein(RNA):
    codon2aa = {"UUU":"F", "CUU":"L", "AUU":"I", "GUU":"V",
                "UUC":"F", "CUC":"L", "AUC":"I", "GUC":"V",
                "UUA":"L", "CUA":"L", "AUA":"I", "GUA":"V",
                "UUG":"L", "CUG":"L", "AUG":"M", "GUG":"V",
                "UCU":"S", "CCU":"P", "ACU":"T", "GCU":"A",
                "UCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
                "UCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
                "UCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
                "UAU":"Y", "CAU":"H", "AAU":"N", "GAU":"D",
                "UAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
                "UAA":"_", "CAA":"Q", "AAA":"K", "GAA":"E",
                "UAG":"_", "CAG":"Q", "AAG":"K", "GAG":"E",
                "UGU":"C", "CGU":"R", "AGU":"S", "GGU":"G",
                "UGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
                "UGA":"_", "CGA":"R", "AGA":"R", "GGA":"G",
                "UGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"}
    protein = ''
    for i in range(0, len(RNA), 3):
        if RNA[i:i+3] in codon2aa:
            protein += codon2aa[RNA[i:i+3]]
    return protein

proteinseq = trans_protein(RNAseq)
endprotein = proteinseq.find('_')
proteinseq = proteinseq[:endprotein]

print(proteinseq)
