# finding reccurence relations in rabbit populations

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
