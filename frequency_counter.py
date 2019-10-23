import random


grades = ['A', 'B', 'C', 'D', 'F']
grades_list = [random.choice(grades) for i in range(11)]

freq = {}
for item in grades_list:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1


print(grades_list)
print(freq)
