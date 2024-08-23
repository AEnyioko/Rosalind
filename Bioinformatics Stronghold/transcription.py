# transcribes DNA to RNA

# my way

def tr(input, output):
    """transcribes rna"""
    n = open(input, "r")
    o = open(output, "w")
    l = n.read()

    for i in l:
        if i == 'T':
            o.write('U')
        else:
            o.write(i)
    o = open(output, "r")
    return o.read()
    
    

print(
tr("Rosalind/Bioinformatics Stronghold/RosalindTxt/rosalind_rna (2).txt", "Rosalind/Bioinformatics Stronghold/transcribed")
    )

# simple way

with open('Rosalind/Bioinformatics Stronghold/RosalindTxt/rosalind_rna (2).txt', 'r') as dna:
    print(str(dna.read().replace('T', 'U')))
