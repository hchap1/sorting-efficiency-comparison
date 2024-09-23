def better_bubble_sort(unsorted):
    running = True
    reverse = False
    while running:
        complete = True
        if reverse:
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
        reverse = not reverse
    return unsorted
