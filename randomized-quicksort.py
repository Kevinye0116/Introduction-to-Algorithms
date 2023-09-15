import random


class RandomQuickSort:
    def random_partition(self, arr, low, high):
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def random_quick_sort(self, arr, low, high):
        if low < high:
            pivot_index = self.random_partition(arr, low, high)
            self.random_quick_sort(arr, low, pivot_index - 1)
            self.random_quick_sort(arr, pivot_index + 1, high)


# Example Testing
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
random_sorter = RandomQuickSort()
random_sorter.random_quick_sort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)
