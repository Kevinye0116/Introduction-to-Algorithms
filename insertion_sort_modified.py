# Insertion_sort modified with Binary_Search
# Reducing the worst running time from Θ(n^2) to Θ(nlgn)

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j]
        arr[left] = key


# Example usage
my_array = [12, 11, 13, 5, 6]
binary_insertion_sort(my_array)
print("Sorted array:", my_array)
