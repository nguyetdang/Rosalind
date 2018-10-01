#!/usr/bin/env python3

### INI3: Strings and Lists

### Given: A string s of length at most 200 letters and four
### integers a, b, c and d

### Return: The slice of this string from indices a through b
### and c through d (with space in between), inclusively. In other
### words, we should include elements s[b] and s[d] in our slice

### Input Strings
path_to_input = input("Input file: ")
f = open(path_to_input, "r")
f1 = f.readlines()
string = f1[0].replace("\n","")
number = f1[1].replace("\n","")
number = number.split(" ")
number = [int(i) for i in number]

### Print the slices

print(string[number[0]:(number[1] + 1)], string[number[2]:(number[3] + 1)])
