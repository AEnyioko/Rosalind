"""
Complementing a Strand of DNA

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

with open('RosalindData/rosalind_revc.txt', 'r') as comp:
    string = str((comp.read()))

    for i in reversed(string):
        if i == 'A':
            print('T', end="")
        elif i == 'T':
            print('A', end="")
        elif i == 'G':
            print('C', end="")
        elif i == 'C':
            print('G', end="")

# a simpler way

# s = 'AAAACCCGGT'
# print(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))