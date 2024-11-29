def longest():
    """
    Longest Increasing Subsequence

    Given: A positive integer n≤10000 followed by a permutation π of length n.

    Return: A longest increasing subsequence of π, 
    followed by a longest decreasing subsequence of π.
    """

perm = [8, 2, 1, 6, 5, 7, 4, 3, 9]

def longest_seq(permutation):
    increasing = []
    i_snapshot = []
    decreasing = []
    d_snapshot = []

    for i in range(len(permutation)):
        increasing.append(permutation[i])
        for j in range(len(increasing)):
            if permutation[i] > increasing[j]:
                i_snapshot.append(increasing[0:-1])
                increasing = increasing[:j]
                increasing.append(permutation[i])
                break

    for i in range(len(permutation)):
        decreasing.append(permutation[i])
        for j in range(len(decreasing)):
            if permutation[i] < decreasing[j]:
                d_snapshot.append(decreasing[:-1])
                decreasing = decreasing[:j]
                decreasing.append(permutation[i])
                break

    print(max(d_snapshot, key=len), max(i_snapshot, key=len))

    return None

longest_seq(perm)