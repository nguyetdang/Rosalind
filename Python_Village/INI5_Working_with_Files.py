#!/usr/bin/env python3

### INI5: Working with Files

### Given: A file containing at most 1000 lines

### Return: A file containing all the even-numbered lines from the
### original file. Assume 1-based numbering of lines

### Input

path_to_input = input("Input file: ")
f_input = open(path_to_input, "r")
f_output = open("rosalind_ini5_out.txt", "w")

lines = f_input.readlines()

i = 1

while i < len(lines) + 1:
    f_output.write(lines[i])
    i = i + 2

f_output.close()
