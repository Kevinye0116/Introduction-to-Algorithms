# Merge_Sort
# Divide-And-Conquer Algorithm --- Recursion

def Merge_Sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = Merge_Sort(left_half)
    right_half = Merge_Sort(right_half)

    return Merge(left_half, right_half)


def Merge(left, right):
    Merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            Merged.append(left[left_idx])
            left_idx += 1
        else:
            Merged.append(right[right_idx])
            right_idx += 1

    Merged.extend(left[left_idx:])
    Merged.extend(right[right_idx:])

    return Merged


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = Merge_Sort(arr)
print("Sorted array:", sorted_arr)
