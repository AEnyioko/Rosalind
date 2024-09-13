def sum_between(a, b):
    """sum between numbers"""
    sum_num = 0
    adding = a

    while adding < b:
        sum_num += adding
        adding += 2
        if adding == b:
            sum_num += b
            break
        else:
            continue
    return sum_num


sum = sum_between(4989, 9634)
print(sum)

