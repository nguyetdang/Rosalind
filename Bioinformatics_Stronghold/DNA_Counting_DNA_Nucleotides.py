#!/usr/bin/env python3

### DNA: Counting DNA Nucleotides

### Given: A DNA string s of length at most 1000 # NOTE:

### Return: Four integers (separated by spaces) counting the respective
### number of times that the symbols 'A', 'C', 'G' and 'T' occur in s

### Input
path_to_input = input("Input file:")
f_input = open(path_to_input, "r")
s = f_input.readline()
s = s.replace("\n","")
s = s.upper()

### Count the number of Nucleotides

A = s.count("A")
C = s.count("C")
G = s.count("G")
T = s.count("T")

print(A, C, G, T)
