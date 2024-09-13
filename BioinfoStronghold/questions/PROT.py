"""
Translating RNA into Protein

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
"""

# super simple way

from Bio.Seq import Seq

with open ('RosalindData/rosalind_prot (1).txt', 'r') as mRNA:
    s = Seq(mRNA.readline())

print(s.translate())
