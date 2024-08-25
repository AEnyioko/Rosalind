"""
Transcribing DNA into RNA

Given: A DNA string 't' having length at most 1000 nt.

Return: The transcribed RNA string of 't'.
"""

def tr(input, output):
    """transcribes rna"""
    n = open(input, "r")
    o = open(output, "w")
    l = n.read()

# exports it to another file

    for i in l:
        if i == 'T':
            o.write('U')
        else:
            o.write(i)
    o = open(output, "r")
    return o.read()
    
print(
tr("RosalindData/rosalind_rna.txt", "Bioinformatics Stronghold/RNA_export")
    )

# simple way

# with open('RosalindData/rosalind_rna.txt', 'r') as dna:
#    print(str(dna.read().replace('T', 'U')))
