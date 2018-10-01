#!/usr/bin/env python3

### INI4: Conditions and Loops

### Given: Two positive integers a and b (a < b < 10000)

### Return: The sum of all odd integers from a through b, inclusively

### Input
path_to_input = input("Input file: ")
f = open(path_to_input, "r")
numbers = f.readline()
numbers = numbers.replace("\n","")
numbers = numbers.split(" ")
numbers = [int(i) for i in numbers]

a = numbers[0]
b = numbers[1]

### If conditions to find the first odd numbers in the list

if a%2 == 0:
    a = a + 1

### While loop to find the sum

sum = 0
while a < (b+1) :
    sum = sum + a
    a = a + 2

print(sum)
