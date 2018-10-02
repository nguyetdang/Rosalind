#!/usr/bin/env python3

### IPRB: Mendel's First Law

### Given: Three positive integers k, m, and n, representing
### a population containing k + m + n organisms: k individuals
### are homozygous dominant, m are heterozygous and n are homozygous
### recessive.

### Return: The probability that two randomly selected mating
### organisms will produce an individuals possessing a dominant
### allele (and thus displaying the dominant phenotype). Assume that
### any two organisms can mate.

### The return value equals 1 - the probrability of obtaining a progenitor
### with recessive genotype

### Input

path_to_input = input("Input file: ")
f_input = open(path_to_input, "r")
numbers = f_input.readline()
numbers = numbers.split(" ")
k = int(numbers[0])
m = int(numbers[1])
n = int(numbers[2])

### Calculate the probrability

total = k + m + n

#### Probability of having all two parents are homozygous recessive
p1 = n/total * (n-1)/(total-1)

#### Probability of having one parents is heterozygous and another
#### is homozygous recessive

p2 = (m/total * n/(total - 1) + n/total * m/(total-1)) * 1/2

#### Probability of having two parents are heterozygous

p3 = (m/total * (m-1)/(total - 1)) * 1/4

#### The final Probability

p = 1 - p1 - p2 - p3

#### Print the result

print(p)
