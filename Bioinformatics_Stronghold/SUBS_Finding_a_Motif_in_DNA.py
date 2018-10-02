#!/usr/bin/env python3

### SUBS: Finding a Motif in codon2aa

### Given: Two DNA strings s and t (each of length at most 1 kbp).

### Return: All locations of t as a substring of s

### Input

path_to_input = input("Input file: ")
f_input = open(path_to_input, "r")
s = f_input.readline().replace("\n","")
t = f_input.readline().replace("\n","")

### Find the index of the motif

i = 0
index = []

while i < (len(s) - len(t)+1):
    if s[i:(i+len(t))] == t:
        index.append(i)
    i = i+1

index = [(i + 1) for i in index]

for i in index:
    print(i, end=" ")
