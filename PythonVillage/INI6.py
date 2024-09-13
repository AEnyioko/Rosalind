w = open("RosalindData/rosalind_ini6.txt", "r")

dictionary = {}

for line in w:
    line_list = line.split()
    for i in line_list:
        num = 0
        key = i
        for i in line_list:
            if i == key:
                num += 1
                dictionary[i] = num
                

for key, value in dictionary.items():
   print(key, value)

w.close()