"""
Finding a Shared Motif

Given: A collection of k(k ≤ 100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""

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
    
    
    i = 0
    j = 999
    substring = strings[0][i:j]
    motif = ''
    for s in strings:
        if substring not in s:
            j -= 1
            if j == 1:
                j == len(strings[0])
                i += 1
            print(substring)

shared('RosalindData/rosalind_lcsm.txt')
