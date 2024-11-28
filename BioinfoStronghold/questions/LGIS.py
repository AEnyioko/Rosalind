def longest():
    """
    Longest Increasing Subsequence

    Given: A positive integer n≤10000 followed by a permutation π of length n.

    Return: A longest increasing subsequence of π, 
    followed by a longest decreasing subsequence of π.
    """

perm = [8, 2, 1, 6, 5, 7, 4, 3, 9]

longest_perm = []
longest_perm.append(perm[0])

for i in range(len(perm)):
    if perm[i] >= longest_perm[-1]:
        continue
    else:
        longest_perm.append(perm[i])

print(longest_perm)