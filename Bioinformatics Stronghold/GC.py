"""
Computing GC Content

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""

# created a dictionary to store sequence name and GC content value

GC_dict = {}

with open('RosalindData/rosalind_gc.txt', 'r') as GC:
    for line in GC.readlines():      
        if '>' in line:
            key = line.strip()
        else:
            value = line.strip()

            if key in GC_dict:
                GC_dict[key].append(value)
            else:
                GC_dict[key] = [value]


# calculates the GC content in each string

def GC_Content(dict):
    """Prints the GC content and the name of the greatest string"""

    Content = {}
    maxi = ''


    for k, v in dict.items():
        a = str(v)
        total = a.count('G') + a.count('C') + a.count('T') + a.count('A')
        GC_count = a.count('G') + a.count('C')
        percentage = GC_count/total*100
        Content[k] = percentage
        
# finds the sequence with the highest value

    maxi = max(Content, key=Content.get)

    return maxi.replace('>', '') + '\n' + str(Content[maxi])

print(GC_Content(GC_dict))
