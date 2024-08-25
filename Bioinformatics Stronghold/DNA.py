"""
Counting DNA Nucleotides

Given: A DNA string s
 of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
"""

# counts the amount of nucleotides

with open("RosalindData/rosalind_dna (1).txt", "r") as f:
    f = f.read()
    numA = f.count('A')
    numC = f.count('C')
    numG = f.count('G')
    numT = f.count('T')

print(numA, numC, numG, numT, end=" ")

# simpler function

def qt(s):
    """Counts nucleotides"""
    return s.count("A"), s.count("G"), s.count("C"), s.count("T")

print(qt(f))

   
   
    