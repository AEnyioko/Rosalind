"""
Enumerating k-mers Lexicographically

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n
(n≤10).

Return: All strings of length n that can be formed from the alphabet,
ordered lexicographically (use the standard order of symbols in the English alphabet).
"""

from itertools import permutations

dna_nuc = "A C G T"
k = 2

perm = permutations(dna_nuc)
print(perm)