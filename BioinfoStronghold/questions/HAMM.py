"""
Counting Point Mutations

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""

# counts the mismatched nucleotides

def point_mutations(file):
    with open(file, 'r') as PM:
        a = PM.readline()
        b = PM.readline()
    count = 0

    for n in range(len(a)):
        if b[n] != a[n]:
            count += 1
    return print(count)


point_mutations('RosalindData/rosalind_hamm.txt')

# simpler way

def hamming(s, t):
    return len(list(filter(lambda pair: pair[0]!=pair[1], zip(s,t))))

