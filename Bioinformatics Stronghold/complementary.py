# prints a complemetary strand of DNA

with open('Rosalind/Bioinformatics Stronghold/RosalindTxt/rosalind_revc (1).txt', 'r') as comp:
    string = str((comp.read()))

    for i in reversed(string):
        if i == 'A':
            print('T', end="")
        elif i == 'T':
            print('A', end="")
        elif i == 'G':
            print('C', end="")
        elif i == 'C':
            print('G', end="")

# a simpler way

s = 'AAAACCCGGT'
print(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))