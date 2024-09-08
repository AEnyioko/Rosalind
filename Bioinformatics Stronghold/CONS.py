"""
Consensus and Profile

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

"""
import numpy as np

with open('RosalindData/rosalind_cons.txt', 'r') as string:
    strings = ''
    for line in string.readlines(): # takes each string a seperates the kbps
        if '>' not in line:
             for n in line:
                strings =  strings + n + ','

a = np.array(strings.split(',')).reshape(7,9) # converts it to array
print(a)
