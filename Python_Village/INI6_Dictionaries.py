#!/usr/bin/env python3

### INI6: Dictionaries

### Given: A string s of length at most 10000 letters

### Return: The number of occurrences of each word in s, where words
### are separated by spaces. Words are case-sensitive, and the
### lines in the output can be in any order.

### Input
path_to_input = input("Input file:")
f_input = open(path_to_input, "r")
s = f_input.readline()
s = s.replace("\n","")
s = s.split(" ")

count = dict((x,s.count(x)) for x in set(s))

### Prepare output
f_output = open("rosalind_ini6_out.txt", "w")

for key, value in count.items():
    print(key, value, file = f_output)

f_output.close()
