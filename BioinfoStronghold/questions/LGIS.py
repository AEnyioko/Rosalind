"""
Longest Increasing Subsequence

Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, 
followed by a longest decreasing subsequence of π.
"""

import bisect

def longest_seq(file):

    with open(file, 'r') as perm:
        old = perm.readlines()[1].strip()
        list_of_permutations = old.split()
        for i in range(len(list_of_permutations)):
            list_of_permutations[i] = int(list_of_permutations[i])

    return None

longest_seq('RosalindData/rosalind_lgis (1).txt')