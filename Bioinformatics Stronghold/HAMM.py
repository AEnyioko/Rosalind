def point_mutations(file):
    with open(file, 'r') as PM:
        a = PM.readline()
        b = PM.readline()
    count = 0

    for n in range(len(a)):
        if b[n] != a[n]:
            count += 1
    return print(count)


point_mutations('Bioinformatics Stronghold/RosalindTxt/rosalind_hamm (1).txt')

# other ways

# sum([a != b for a, b in zip(s1, s2)])

def hamming(s, t):
    return len(list(filter(lambda pair: pair[0]!=pair[1], zip(s,t))))

