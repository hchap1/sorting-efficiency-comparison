import random

with open("testcases.txt", 'w') as f:
    size = 1
    while size <= 1000:
        random_list = [random.randint(1, 100) for _ in range(size)]
        f.write(', '.join(map(str, random_list)) + '\n')
        size += 10
