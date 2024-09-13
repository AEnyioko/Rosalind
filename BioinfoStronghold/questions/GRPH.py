"""
Overlap Graphs

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
"""

def overlap(file, Ok):
    # puts keys and strings in their lists
    keys = []
    strings = []
    string = ''
    with open(file, 'r') as overlap:
        for line in overlap.readlines():
            if '>' not in line:
                string += line.strip()
            else:
                keys.append(line.strip())
                if string != '':
                    strings.append(string)
                    string = ''

    # checks if suffix of string 1 = prefix of string 2; prints their keys if they do
    for i in range(len(strings)):
        for n in range(len(strings)):
            if strings[i][-Ok:] == strings[n][:Ok]:
                if strings[i] != strings[n]:
                    print(keys[i][1:] + ' ' + keys[n][1:])
    

overlap('RosalindData/rosalind_grph (3).txt', 3)
        

