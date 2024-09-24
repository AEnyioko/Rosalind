"""
Calculating Expected Offspring

Given: Six nonnegative integers, each of which does not exceed 20,000. 
The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. 
In order, the six given integers represent the number of couples having the following genotypes:
1. AA-AA
2. AA-Aa
3. AA-aa
4. Aa-Aa
5. Aa-aa
6. aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, 
under the assumption that every couple has exactly two offspring.
"""

couples = {1: 1, 2: 1, 3: 1, 4: 0.75, 5: 0.5, 6: 0}
offspring = [19992, 19579, 16055, 16655, 19422, 18434]


constant = 0
sum = 0
for i in range(len(offspring)):
    sum = offspring[i] * couples[i + 1]
    constant += sum

print(2 * constant)