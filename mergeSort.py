
def merge(left, right):
    i, j = 0, 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def merge_sort(elements):
    if len(elements) <= 1:
        return elements
    middle = int(len(elements) / 2)
    sorted_left = merge_sort(elements[:middle])
    sorted_right = merge_sort(elements[middle:])

    return merge(sorted_left, sorted_right)
