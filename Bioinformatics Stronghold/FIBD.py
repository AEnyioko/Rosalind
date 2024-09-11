"""
Mortal Fibonacci Rabbits

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""

def mortal_fibonacci_rabbits(m, n):  
    F = [0] * n
    F[0] = 1  

    for month in range(m-1): 
        newborns = sum(F[1:])  
        F = [newborns] + F[:-1]
    return sum(F)

print(mortal_fibonacci_rabbits(6, 3))
