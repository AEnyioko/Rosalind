"""
Consensus and Profile

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

"""

import numpy as np

with open('RosalindData/rosalind_cons.txt', 'r') as strings:

    s = ""
    for line in strings.readlines():      
        if '>' in line:
            key = line.strip()
        else:
            value = line.strip()
            s += (value + "; ") 


print(s)
