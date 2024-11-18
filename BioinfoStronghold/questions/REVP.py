"""
Locating Restriction Sites

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string
having length between 4 and 12. You may return these pairs in any order.
"""
from Bio.Seq import Seq

def restriction_sites(file):
    string = ''
    with open(file, 'r') as dna:
        next(dna) # skips first line
        for line in dna:
            string += line.strip() # puts sequence into a string
    
    for i in range(len(string)):
        for j in range(4, 13): # checks for palindromes of lenght j at position i
            if i + j > len(string): # skips repeats and small palindromes
                continue
            substring = string[i:i+j]
            if Seq(substring).reverse_complement() == Seq(substring): # checks if substring is a palindrome
                print(f"{i+1} {j} {substring}")

    return None

restriction_sites('RosalindData/rosalind_revp (1).txt')