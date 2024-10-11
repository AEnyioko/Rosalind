"""
Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
"""
from Bio.Seq import Seq

def open_reading_frames(file):
    stop_codons = ['UAA', 'UAG', 'UGA']
    start_codon = 'AUG'
    seq = ''
    reading_frames = []

    # puts FASTA in string
    with open(file, 'r') as dna:
       for line in dna.readlines()[1:]:
            seq += line.strip()

    rna = Seq(seq).transcribe()

    # locates the frames

    def find_frames(sequence):
        orfs = []
        for i in range(len(sequence)):
            if sequence[i:i+3] == start_codon:
                for j in range(i, len(sequence), 3):
                    stop = sequence[j:j+3]
                    if stop in stop_codons:
                        orfs.append(sequence[i:j+3])
                        break

        return orfs

# creates frames
    for i in range(3):
        forward_frames = (find_frames(rna[i:]))
        reading_frames.extend(forward_frames)

    reversedrna = rna.reverse_complement()
    for i in range(3):
        reverse_frames = (find_frames(reversedrna[i:]))
        reading_frames.extend(reverse_frames)

# reads all 3 reading frames
    proteins = []
    for frame in reading_frames:
        proteins.append(str(Seq(frame).translate()))

    return proteins
        
for protein in open_reading_frames('RosalindData/rosalind_orf (5).txt'):
    print(protein)