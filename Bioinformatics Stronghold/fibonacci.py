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

fibonacci(28, 2)

# mortal fibonacci rabbits

def mortal_fibonacci(curr_month, lifespan):
    """generational offspring calc"""

    count = 0
    pop = 0

    for i in range(curr_month + 1):
        if i >= 2:
            if i % lifespan != 0:
                pop = fibonacci(curr_month, 1)
            else:
                count += 1
                pop -= lifespan*count
            print(i, pop)

    return print(pop)

mortal_fibonacci(7, 3)
