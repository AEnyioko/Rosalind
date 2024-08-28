"""
Computing GC Content

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""

# created a dictionary to store sequence name and GC content value

def GC_Content(dict):
    """Prints the name and value of the sequence with the highest GC content"""

    GC_dict = {}
    with open(dict, 'r') as GC:
        for line in GC.readlines():      
            if '>' in line:
                key = line.strip()
            else:
                value = line.strip()

                if key in GC_dict:
                    GC_dict[key].append(value)
                else:
                    GC_dict[key] = [value]

    Content = {}
    maxi = ''

# calculates the GC content in each string

    for k, v in GC_dict.items():
        a = str(v)
        total = a.count('G') + a.count('C') + a.count('T') + a.count('A')
        GC_count = a.count('G') + a.count('C')
        percentage = GC_count/total*100
        Content[k] = percentage
        
# finds the sequence with the highest value

    maxi = max(Content, key=Content.get)

    return maxi.replace('>', '') + '\n' + str(Content[maxi])

print(GC_Content('RosalindData/rosalind_gc.txt'))
