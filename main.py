from insertion_sort import insertion_sort
from merge_sort import merge_sort
from counting_sort import counting_sort
from bubble_sort import bubble_sort
from alternative_bubble_sort import alternative_bubble_sort
from better_better_bubble_sort import better_better_bubble_sort
from cocktail_sort import better_bubble_sort
from graph import graph
from time import perf_counter

total_time = 0
max_time = 0
verify = True

def measure(func, unsorted):
    temp_list = unsorted.copy()
    start = perf_counter()
    res = func(temp_list)
    end = perf_counter()
    if verify:
        valid = True
        for n in range(1, len(res)):
            if res[n] < res[n-1]:
                valid = False
        if not valid:
            print(f"FAILED: {func.__name__}")
    return (end - start) * 1000

def find_runtime(func, testcases):
    global max_time, total_time
    times = [func.__name__]
    for testcase in testcases:
        n = len(testcase)
        t = measure(func, testcase)
        total_time += t
        times.append((n, t))
        if t > max_time:
            max_time = t
    return times

with open("testcases.txt", "r") as data:
    testcases = [[int(y) for y in x.strip("\n").split(", ")] for x in data.readlines()]

functions_to_test = [insertion_sort]
sets = []
for func in functions_to_test:
    sets.append(find_runtime(func, testcases))
graph(sets, len(testcases[-1]), total_time / len(functions_to_test) / len(functions_to_test) / 10)
