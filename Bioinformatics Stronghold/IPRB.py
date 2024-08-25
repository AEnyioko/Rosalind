"""
Mendel's First Law

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
- k individuals are homozygous dominant for a factor
- m are heterozygous
- n are homozygous recessive

Return: The probability that two randomly selected mating organisms will produce
an individual possessing a dominant allele (and thus displaying the dominant phenotype).
Assume that any two organisms can mate.
"""

import random

def mendel(x, y, z):
    #calculate the probability of recessive traits only
    total = x+y+z
    twoRecess = (z/total)*((z-1)/(total-1))
    twoHetero = (y/total)*((y-1)/(total-1))
    heteroRecess = (z/total)*(y/(total-1)) + (y/total)*(z/(total-1))

    recessProb = twoRecess + twoHetero*1/4 + heteroRecess*1/2
    print(1-recessProb) # take the complement

mendel(2, 2, 2)
