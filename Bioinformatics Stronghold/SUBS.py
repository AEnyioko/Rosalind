"""
Finding a Motif in DNA

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""

def motif(s_file):

    # sorts strings
    f = open(s_file, 'r')
    seq = f.readline().strip()
    motif = f.readline().strip()


    # checks for motif sequence across each kbp in main string 
    for i in range(len(seq)):
        if motif[0:len(motif)] == seq[i:i + len(motif)]:
           print(i + 1, end=', ')
    
motif('RosalindData/rosalind_subs.txt')