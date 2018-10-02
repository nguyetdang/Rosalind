#!/usr/bin/env python3

### FIB: Rabbits and Recurrence Relations

### Given: Positive integers n <= 40 and k <= 5

### Return: The total number of rabbit pairs that will be
### present after n months, if we begin with 1 pair and in
### each generation, every pair of reproduction-age rabbits
### produces a litter of k rabbit pairs (instead of only 1 pair)

### Input

path_to_input = input("Input file: ")
f_input = open(path_to_input, "r")
numbers = f_input.readline()
numbers = numbers.replace("\n","")
numbers = numbers.split(" ")
n = int(numbers[0])
k = int(numbers[1])

### Calculate numbers of rabbits after each month
### and save the results in a list

rabbits = [1,1]
i = 3
while (i <= n):
    rabbits.append(rabbits[i-3]*k + rabbits[i-2])
    i = i + 1

print(rabbits[n-1])
