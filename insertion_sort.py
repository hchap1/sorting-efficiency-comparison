def insertion_sort(unsorted):
    sorted = []
    for item in unsorted:
        emplaced = False
        for idx, val in enumerate(sorted):
            if item < val:
                sorted.insert(idx, item)
                emplaced = True
                break
        if not emplaced:
            sorted.append(item)
    return sorted
