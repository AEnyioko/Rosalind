"""
Finding a Shared Motif

Given: A collection of k(k ≤ 100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""

def shared(file):
    # puts keys and strings in their lists
    sdict = {}
    string = ''
    with open(file, 'r') as overlap:
        for line in overlap.readlines():
            if '>' not in line:
                string += line.strip()
            else:
                key = line.strip()
                if key in sdict:
                    sdict[key].append(string)
                else:
                    if string != '':
                        sdict[key] = string
                        string = ''
    sequence = ''
    for s in sdict.values():
        sequence = s[0]
    print(sequence)
    
print(shared('RosalindData/rosalind_lcsm.txt'))
