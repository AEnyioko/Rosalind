"""
Finding a Shared Motif

Given: A collection of k(k ≤ 100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""
from itertools import combinations

def shared(file):
    # puts keys and strings in their lists
    strings = []
    string = ''
    with open(file, 'r') as overlap:
        for line in overlap.readlines():
            if '>' in line:
                strings.append(string)
                string = ''
            else:
                string += line.strip()   
    del strings[0]
    strings.append(string)
    
    main_string = strings[0]
    substring = sorted([main_string[x:y] for x, y in combinations(
        range(len(main_string) + 1), r = 2)], key=len)

    print(substring[0:10].reverse())

    for s in strings:
        for ss in reversed(substring):
            if ss not in strings:
                continue
            else:
                if s == strings[-1]:
                    print(ss)
        
    return None

shared('RosalindData/rosalind_lcsm.txt')
