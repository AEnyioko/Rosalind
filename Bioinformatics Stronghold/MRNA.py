"""
Inferring mRNA from Protein

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. 
(Don't neglect the importance of the stop codon in protein translation.)
"""

from Bio.Seq import Seq, CodonTable

# obtain protein seq

protein_seq = Seq('MA')
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]

# identify sequences

for protein in protein_seq:
    print(standard_table.columns)
