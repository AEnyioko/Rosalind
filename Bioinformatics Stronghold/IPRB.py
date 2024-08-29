"""
Mendel's First Law

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
- k individuals are homozygous dominant for a factor
- m are heterozygous
- n are homozygous recessive

Return: The probability that two randomly selected mating organisms will produce
an individual possessing a dominant allele (and thus displaying the dominant phenotype).
Assume that any two organisms can mate.
"""

def mendel(k, m, n):
    # gets the total
    total = k + m + n

    # calculates the chances of each combination
    tworec = (n/total)*((n - 1)/(total - 1))
    twohetero = (m/total)*((m - 1)/(total - 1))
    hetrec = (n/total)*(m/(total - 1)) + (m/total)*(n/(total - 1))

    # gets probability of recessive phenotype occuring
    prob = tworec + twohetero*(1/4) + hetrec*(1/2)

    #finds dominant by subtracting recessive from pop
    return 1 - prob

print(mendel(20, 20, 30))

