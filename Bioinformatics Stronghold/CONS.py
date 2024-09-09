"""
Consensus and Profile

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

"""

import numpy as np

with open('RosalindData/rosalind_cons (2).txt', 'r') as string:
    strings = ''
    count = 0

    for line in string.readlines(): # takes each string a seperates the kbps
        if '>' in line:
            if count == 0:
                key = line.strip()
                count += 1         
            else:
                count += 1
                strings += ','
                
        else:
            value = line.strip()
            strings += (value)

g = round(len(strings[0:len(strings) - 1])/(count - 1))


a = np.array(strings.split(',')) # converts it to array
print(a)
pm_dict = {
                    'A': [], 
                    'C': [], 
                    'G': [], 
                    'T': []
                  } 


for n in range(g): # creates profile matrix array and stores in dict
    s = ''
    for i in range(len(a)):
        s = s + (a[i][n])
    count = s.count("A"), s.count("C"), s.count("G"), s.count("T")
    c = 0
    for i in pm_dict.keys():
        pm_dict.setdefault(i, [])
        pm_dict[i].append(count[c])  
        c += 1   

pm_array = []
for i in pm_dict.keys():
    pm_array.append(pm_dict[i])

f = np.array(pm_array)

# Find the indices of the maximum values along each column (axis=0)
row_indices_of_max = np.argmax(f, axis=0)

print(str(row_indices_of_max).translate(str.maketrans('0123', 'ACGT')))
print(f)
