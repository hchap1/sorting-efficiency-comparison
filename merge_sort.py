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

def merge_sort(unsorted):
    a, b = split_list(unsorted) 
    if len(a) > 1 or len(b) > 1:
        return merge(merge_sort(a), merge_sort(b))
    return merge(a, b)
