#!/usr/bin/env python3

### REVC: Complementing a Strand of DNA

### Given: A DNA string s of length at most 1000 bp

### Return: The reverse complement of s

### Input

path_to_input = input("Input file: ")
f_input = open(path_to_input, "r")
DNA = f_input.readline()
DNA = DNA.replace("\n","")
DNA = DNA.upper()

### Reverse complement

def reverse_complement(DNA):
    complement = {"A" : "T", "C" : "G", "G" : "C", "T" : "A"}
    return ''.join(complement[base] for base in DNA[::-1])

revc_DNA = reverse_complement(DNA)
print(revc_DNA)
