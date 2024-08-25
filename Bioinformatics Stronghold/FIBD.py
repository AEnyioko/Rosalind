# mortal fibonacci rabbits

def mortal_fibonacci(curr_month, lifespan):
    """generational offspring calc"""

    count = 0
    pop = 0

    for i in range(curr_month + 1):
        if i >= 2:
            if i % lifespan != 0:
                pop = (curr_month, 1)
            else:
                count += 1
                pop -= lifespan*count
            print(i, pop)

    return print(pop)

mortal_fibonacci(7, 3)
