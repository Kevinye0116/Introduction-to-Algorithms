import random


def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)
    left_length = pivot_index - low + 1

    if k == left_length:
        return arr[pivot_index]
    elif k < left_length:
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, high, k - left_length)


# Example Test
arr = [3, 1, 9, 5, 7, 2, 8]
k = 4
result = randomized_select(arr, 0, len(arr) - 1, k)
print(f"The {k}-th smallest element is {result}")
