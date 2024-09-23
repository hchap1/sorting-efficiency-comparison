def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def merge(a, b):
    na = len(a)
    nb = len(b)
    merged = []
    idx_a = 0
    idx_b = 0
    skip_next = False
    for _ in range(na + nb - 1):
        if skip_next:
            skip_next = False
            continue
        if idx_a >= na or idx_b >= nb:
            break
        if a[idx_a] < b[idx_b]:
            merged.append(a[idx_a])
            idx_a += 1
        elif a[idx_a] > b[idx_b]:
            merged.append(b[idx_b])
            idx_b += 1
        else:
            merged.append(a[idx_a])
            merged.append(b[idx_b])
            idx_a += 1
            idx_b += 1
            skip_next = True
    if idx_a < na:
        while idx_a < na:
            merged.append(a[idx_a])
            idx_a += 1
    if idx_b < nb:
        while idx_b < nb:
            merged.append(b[idx_b])
            idx_b += 1
    return merged

def bubble_sort(unsorted):
    running = True
    while running:
        complete = True
        for n in range(1, len(unsorted)):
            if unsorted[n] < unsorted[n-1]:
                temp = unsorted[n-1]
                unsorted[n-1] = unsorted[n]
                unsorted[n] = temp
                complete = False
        if complete: running = False
    return sorted

def better_better_bubble_sort(unsorted):
    a, b = split_list(unsorted)     
    bubble_sort(a)
    bubble_sort(b)
    return merge(a, b)
