"""
Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.
"""

def cpm(file):

    # monoisotopic masses
    mass_table = {
    'A':   71.03711, 'C':   103.00919, 'D':   115.02694, 'E':   129.04259,
    'F':   147.06841, 'G':   57.02146, 'H':   137.05891, 'I':   113.08406, 
    'K':   128.09496, 'L':   113.08406, 'M':   131.04049, 'N':   114.04293,
    'P':   97.05276, 'Q':   128.05858, 'R':   156.10111, 'S':   87.03203,
    'T':   101.04768, 'V':   99.06841, 'W':   186.07931, 'Y':   163.06333
    }

    # grabs file and holds string 
    prot = ''
    with open(file, 'r') as cpm:
        for line in cpm:
            prot += line.strip()

    # calculates weight of each protein
    weight = 0
    for char in prot:
        weight += mass_table[char]

    return weight

print(cpm('RosalindData/rosalind_prtm.txt'))