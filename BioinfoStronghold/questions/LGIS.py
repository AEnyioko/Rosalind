"""
Longest Increasing Subsequence

Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, 
followed by a longest decreasing subsequence of π.
"""

import bisect

def longest_seq(file):
    numbers = []
    with open(file, 'r') as perm:
        length = int(perm.readline().strip())
        for line in perm.readline().split():
            numbers.append(int(line))

    # longest increasing subsequence
    longest = []
    
 
    return length, numbers

a = longest_seq('RosalindData/rosalind_lgis (1).txt')
print(a)