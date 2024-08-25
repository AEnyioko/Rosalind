# transcribes DNA to RNA
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
tr("RosalindData/rosalind_rna.txt", "Bioinformatics Stronghold/transcribed")
    )

# simple way

# with open('RosalindData/rosalind_rna.txt', 'r') as dna:
#    print(str(dna.read().replace('T', 'U')))
