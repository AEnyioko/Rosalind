"""
Consensus and Profile

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

"""

import numpy as np
import sys

def cons_prof(file):
    with open(file, 'r') as string:
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
    rows = str(row_indices_of_max).translate(str.maketrans('0123', 'ACGT'))
    ans = ''
    for l in rows:
        ans = ans + l.strip()

    # puts the profile matrix into a string
    apm = ''
    for l in f[0]:
        apm = apm + str(l) + ' '

    cpm = ''
    for l in f[1]:
        cpm = cpm + str(l) + ' '

    gpm = ''
    for l in f[2]:
        gpm = gpm + str(l) + ' '

    tpm = ''
    for l in f[3]:
        tpm = tpm + str(l) + ' '

    # exports the answer to a text file
    sys.stdout = open('ans.txt', 'w')
    print(str(ans)[1:-1])
    print('A: ' + apm)
    print('C: ' + cpm)
    print('G: ' + gpm)
    print('T: ' + tpm)
    sys.stdout.close()

cons_prof('RosalindData/rosalind_cons (6).txt')
