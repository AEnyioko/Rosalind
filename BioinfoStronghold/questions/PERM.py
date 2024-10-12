"""
Given: A positive integer n≤7.

Return: The total number of permutations of length n, 
followed by a list of all such permutations (in any order).
"""

from itertools import permutations
from math import factorial

def ego(number):
    # generates list of permutations and the amount of them
    n_of_perms = factorial(number)
    s = permutations([i for i in range(1, number + 1)])

    # sends to file
    with open('BioinfoStronghold/exports/PERM.txt', 'w') as perm:
        perm.write(str(n_of_perms) + '\n')
        for i in s: 
            perm.write((str(i)[1:-1]).replace(',','') + '\n')
    perm.close()

    return n_of_perms

ego(6)


