"""
Given: A DNA string s (of length at most 1 kbp) 
and a collection of substrings of s
acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and 
translating the exons of s. 
(Note: Only one solution will exist for the dataset provided.)
"""

from Bio import SeqIO
from Bio.Seq import Seq

def rna_splicing(file):

    # parses the file and gets the dna string
    records = SeqIO.parse(file,'fasta')
    dna = str(next(records).seq)
    introns = []

    # collects the introns
    for record in records:
        introns.append(str(record.seq))                  
    
    # splices the introns from the dna string
    for intron in introns:
        dna = dna.replace(intron, '')

    # translates the protein string
    protein_string = Seq(dna).translate()

    return protein_string.replace('*', '')

print(rna_splicing('RosalindData/rosalind_splc (2).txt'))