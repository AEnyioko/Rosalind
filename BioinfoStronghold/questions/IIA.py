"""
Independent Alleles

Given: Two positive integers k(k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. 
Tom has two children in the 1st generation, each of whom has two children, and so on. 
Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree 
(don't count the Aa Bb mates at each level). 
Assume that Mendel's second law holds for the factors.
"""
import scipy.stats as stats

def prob(gen, success):
    # total offspring and Aa Bb phenotype chance
    n = 2 ** gen 
    chance = 0.25

    # cumulative probability of getting non-Aa Bb offspring in <= success offspring
    cumulative_prob = stats.binom.cdf(success - 1, n, chance)

    # 1 - chance of failure = least chance of success
    at_least_prob = 1 - cumulative_prob

    return at_least_prob

print(prob(5, 9))

