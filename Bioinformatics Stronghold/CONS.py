"""
Consensus and Profile

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

"""

import numpy as np

with open('RosalindData/rosalind_cons (3).txt', 'r') as string:
    strings = ''
    count = 0
    strlen = 0

# takes each string a seperates the kbps
    for line in string.readlines(): 
        if '>' in line:
            if count == 0:
                key = line.strip()
                count += 1         
            else:
                count += 1
                strings += ','
                
        else:
            value = line.strip()
            for n in line.strip():
                strlen += 1
                strings += (n + ',')

# gets the len of the strings to find array row length
arraxis = round(strlen/count) 

# converts it to array
a = np.array(strings.split(',')).reshape(count, (arraxis + 1)) 

pm_dict = {
                    'A': [], 
                    'C': [], 
                    'G': [], 
                    'T': []
                  } 

# creates profile matrix by making a dict and turning it into an array
for n in range(arraxis): 
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

# stores the array
f = np.array(pm_array)

# Find the indices of the maximum values along each column (axis=0)
row_indices_of_max = np.argmax(f, axis=0)

# gets the consensus string from translating the row value to the corresponding kbp
ans = str(row_indices_of_max).translate(str.maketrans('0123', 'ACGT'))

print(str(ans)[1:-1])
print(f)
