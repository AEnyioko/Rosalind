couples = {1: 1, 2: 1, 3: 1, 4: 0.75, 5: 0.5, 6: 0}
offspring = [19992, 19579, 16055, 16655, 19422, 18434]


constant = 0
sum = 0
for i in range(len(offspring)):
    sum = offspring[i] * couples[i + 1]
    constant += sum

print(2 * constant)