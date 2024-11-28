"""
Finding a Shared Motif

Given: A collection of k(k ≤ 100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""
from itertools import combinations

def shared(file):
    # puts keys and strings in their lists
    strings = []
    string = ''
    with open(file, 'r') as overlap:
        for line in overlap.readlines():
            if '>' in line:
                strings.append(string)
                string = ''
            else:
                string += line.strip()   
    del strings[0]
    strings.append(string)
    
    # generates substrings and sorts them based on length
    main_string = strings[0]
    substring = sorted([main_string[x:y] for x, y in combinations(
        range(len(main_string) + 1), r = 2)], key=len)
    
    
    
    # checks if substrings is in all strings going from largest to smallest substring
    flag = True
    for n in substring[::-1]:
        for s in strings:
            if n in s:
                if flag == False:
                    break
                else:
                    if s == strings[-1]:
                        print(n)
                        flag = False
            else:
                continue
                    

    #improvements to make: 
    #simpler logic for flag system
    #check 1 substring and shrink instead of checking all possible
        #less processing strain
        #more efficient
        #create scenario if no common string found

    
shared('RosalindData/rosalind_lcsm (1).txt')
