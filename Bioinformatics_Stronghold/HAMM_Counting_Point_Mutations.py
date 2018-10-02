#!/usr/bin/env python3

### HAMM: Counting Point Mutations

### Given: Two DNA strings s and t of equal length (not
### exceeding 1 kbp).

### Return: The Hamming distance dH(s,t)

### Input

path_to_input = input("Input file: ")
f_input = open(path_to_input, "r")
seq1 = f_input.readline()
seq2 = f_input.readline()

### Calculate the Hamming distance
i = 0
HAMM = 0
while i < len(seq1):
    if seq1[i] == seq2[i]:
        HAMM = HAMM
    else:
        HAMM = HAMM + 1
    i = i + 1

print(HAMM)
