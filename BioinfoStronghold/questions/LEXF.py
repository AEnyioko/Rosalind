"""
Enumerating k-mers Lexicographically

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n
(n≤10).

Return: All strings of length n that can be formed from the alphabet,
ordered lexicographically (use the standard order of symbols in the English alphabet).
"""

from itertools import product

def k_values(file):
    #reads file
    with open(file, 'r') as k:
        symbols = k.readline().strip().split()
        size = int(k.readline().strip())

    #prints values
    k_mers = product(symbols, repeat=size)

    return k_mers
    
for i in k_values('RosalindData/rosalind_lexf (1).txt'):
    k_mer = ''
    for n in i:
        k_mer += n
    print(k_mer)