GC_dict = {}

with open('Rosalind/Bioinformatics Stronghold/RosalindTxt/rosalind_gc (2).txt', 'r') as GC:
    for line in GC.readlines():      
        if '>' in line:
            key = line.strip()
        else:
            value = line.strip()

            if key in GC_dict:
                GC_dict[key].append(value)
            else:
                GC_dict[key] = [value]



def GC_Content(dict):
    """Calculates GC Content in a dictionary"""

    Content = {}
    maxi = ''


    for k, v in dict.items():
        a = str(v)
        total = a.count('G') + a.count('C') + a.count('T') + a.count('A')
        GC_count = a.count('G') + a.count('C')
        percentage = GC_count/total*100
        Content[k] = percentage
        

    maxi = max(Content, key=Content.get)

    return print(maxi.replace('>', '') + '\n' + str(Content[maxi]))

GC_Content(GC_dict)

 