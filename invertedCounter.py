def merge_and_count_split_inv(left, right):
    i, j = 0, 0
    split_inv = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            split_inv += len(left) - i

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, split_inv


def count_inversions(elements):
    if len(elements) <= 1:
        return elements, 0
    middle = int(len(elements) / 2)
    left_sorted, left_inverted = count_inversions(elements[:middle])
    right_sorted, right_inverted = count_inversions(elements[middle:])
    elem_sorted, split_inverted = merge_and_count_split_inv(left_sorted, right_sorted)
    return elem_sorted, left_inverted + right_inverted + split_inverted


def total_count(elements):
    sorty, count = count_inversions([int(line) for line in elements])
    return count
