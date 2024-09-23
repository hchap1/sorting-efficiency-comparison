def bubble_sort(unsorted):
    sorted = unsorted.copy()
    running = True
    while running:
        complete = True
        for n in range(1, len(sorted)):
            if sorted[n] < sorted[n-1]:
                temp = sorted[n-1]
                sorted[n-1] = sorted[n]
                sorted[n] = temp
                complete = False
        if complete: running = False
    return sorted
