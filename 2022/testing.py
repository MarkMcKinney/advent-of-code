import time
import day1 as d1

# Testing Config #
test_rounds = 10000
solutions_to_test = [
    d1.getMaxCalorieMark, # 0.0005901309967041015 ms
    d1.getMaxCalorieMark_Optimized, # 0.00038572840690612794 ms !!!
    d1.getMaxCalorieJonathanPaulson, # 0.0004540848970413208 ms
    d1.getMaxCalorieAkaruiYami # 0.0012166382789611815 ms
]

# Test each solution
for solution in solutions_to_test:
    start_time = time.time()
    i = 0
    while i < test_rounds:
        solution()
        i += 1
    print((time.time() - start_time)/test_rounds)