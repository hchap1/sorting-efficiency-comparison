def alternative_bubble_sort(unsorted):
    running = True
    first_half = unsorted[0]
    second_half = 0
    for n in range(1, len(unsorted)):
        if n <= len(unsorted) / 2:
            first_half += n
        else: second_half += n
    # How many normals should be performed per reverse
    ratio = 2 * int(first_half / second_half)
    count = 0
    max = ratio + 2
    while running:
        complete = True
        if count <= ratio:
            for n in range(len(unsorted)-1, 0, -1):
                if unsorted[n] < unsorted[n-1]:
                    temp = unsorted[n-1]
                    unsorted[n-1] = unsorted[n]
                    unsorted[n] = temp
                    complete = False
        else:
            for n in range(1, len(unsorted)):
                if unsorted[n] < unsorted[n-1]:
                    temp = unsorted[n-1]
                    unsorted[n-1] = unsorted[n]
                    unsorted[n] = temp
                    complete = False
        if complete: running = False
        count += 1
        if count == max:
            count = 0
    return unsorted
