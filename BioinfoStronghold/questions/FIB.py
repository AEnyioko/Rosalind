"""
Rabbits and Recurrence Relations

Given: Positive integers n≤40
 and k≤5.

Return: The total number of rabbit pairs that will be present after n
 months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
 rabbit pairs (instead of only 1 pair).
"""


def fibonacci(months, pairs):
    """generational offspring calc"""
    grand_gen = 1
    prev_gen = 1
    curr_gen = 1

    for n in range(months + 1):
        if n > 2:
            curr_gen = grand_gen*pairs + prev_gen
            grand_gen = prev_gen
            prev_gen = curr_gen

    return curr_gen

print(fibonacci(28, 2))
