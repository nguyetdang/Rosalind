#!/usr/bin/env python3

### RNA: Transcribing DNA into RNA

### Given: A DNA string t having length at most 1000 nt

### Return: The transcribed RNA string of t

### Input

path_to_input = input("Input file: ")
f_input = open(path_to_input, "r")
t = f_input.readline()
t = t.replace("\n","")
t = t.upper()

### Transcribe into RNA

RNA = t.replace("T","U")
print(RNA)
