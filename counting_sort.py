def counting_sort(unsorted):
    k = max(unsorted)
    sorted = []
    c = [0] * (k + 1)
    sorted = [0] * len(unsorted)
    for i in unsorted:
        c[i] += 1
    for i in range(1, k + 1):
        c[i] += c[i - 1]
    for i in range(len(unsorted) - 1, -1, -1):
        sorted[c[unsorted[i]] - 1] = unsorted[i]
        c[unsorted[i]] -= 1
    return sorted
