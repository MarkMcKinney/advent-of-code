import os

# MY FIRST SOLUTION
# Avg duration after 10k executions: 0.0005901309967041015 ms
def getMaxCalorieMark():
    with open('day1.txt') as f:
        elves_array = f.readlines()
    total_cal = 0
    elves_totals = []
    i = 1
    for count in elves_array:
        fmt_count = count.split("\n")[0]
        if fmt_count != '':
            total_cal += int(fmt_count)
        else:
            elves_totals.append(total_cal)
            total_cal = 0
        if len(elves_array) == i:
            elves_totals.append(total_cal)
            total_cal = 0
        i += 1
    elves_totals.sort(reverse=True)
    return [elves_totals[0], sum(elves_totals[0:3])]

# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/1.py
# Avg duration after 10k executions: 0.0004540848970413208 ms
def getMaxCalorieJonathanPaulson():
    X = [l.strip() for l in open('day1.txt')] # Smart use of list comprehension
    Q = []
    for elf in ('\n'.join(X)).split('\n\n'):
        q = 0
        for x in elf.split('\n'):
            q += int(x)
        Q.append(q)
    Q = sorted(Q)
    return(Q[-1],Q[-1]+Q[-2]+Q[-3])

# https://github.com/AkaruiYami/AdventOfCode2022/blob/main/D01/main.py
# Avg duration after 10k executions: 0.0012166382789611815 ms
def getMaxCalorieAkaruiYami():
    # Find dir address where the current code located and read input.txt from the dir
    dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(dir, "day1.txt")) as file:
        data = file.read().split("\n\n")

    elves = [eval(_data.replace("\n", "+")) for _data in data] # Really interesting use of list comprehension, but too slow

    return(max(elves.copy()), sum(elves.copy()[:3]))

'''
MY IMPROVED SOLUTION
# Avg duration after 10k executions: 0.00038572840690612794 ms - BEST
- Just using list comprehension and removing another split() reduced time by 14%!
- Remove the last total check in the loop, append it if != 0 outside of loop
    > This means 1 less split(), 1 less conditional, and 2 less var modifications
- Total improvement: 33%
'''
def getMaxCalorieMark_Optimized():
    
    calories = [l.strip() for l in open('day1.txt')]
    elves_totals = []
    total_cal = 0

    for count in calories:
        if count != '':
            total_cal += int(count)
        else:
            elves_totals.append(total_cal)
            total_cal = 0

    # Append the last total after the last \n\n (if any)
    if total_cal != 0:
        elves_totals.append(total_cal)
    elves_totals.sort(reverse=True)
    return [elves_totals[0], (elves_totals[0]+elves_totals[1]+elves_totals[2])]

'''
LEARNING RECAP
- Use list comprehension if the end result will be an array
- Use string manipulation functions within the list comprehension
- Remove as many additional string manipulation functions outside of that list comprehension as possible (e.g. split())
- The solution with the least amount of steps isn't always the most efficient
'''