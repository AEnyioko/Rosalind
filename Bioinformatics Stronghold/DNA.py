# counts the amount of nucleotides

with open("Bioinformatics Stronghold/RosalindTxt/rosalind_dna (1).txt", "r") as f:
    f = f.read()
    numA = f.count('A')
    numC = f.count('C')
    numG = f.count('G')
    numT = f.count('T')

print(numA, numC, numG, numT, end=" ")

# simpler function

def qt(s):
    """Counts nucleotides"""
    return s.count("A"), s.count("G"), s.count("C"), s.count("T")

print(qt(f))

   
   
    