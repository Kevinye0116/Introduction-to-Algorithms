class Quick_Sort:
    def __init__(self, arr):
        self.arr = arr

    def quick_sort(self, low=0, high=None):
        if high is None:
            high = len(self.arr) - 1

        if low < high:
            partition_index = self.partition(low, high)
            self.quick_sort(low, partition_index - 1)
            self.quick_sort(partition_index + 1, high)

    def partition(self, low, high):
        pivot = self.arr[high]
        i = low - 1

        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1


# Example Testing
if __name__ == "__main__":
    input_array = [64, 34, 25, 12, 22, 11, 90]
    sorter = Quick_Sort(input_array)
    sorter.quick_sort()
    sorted_array = sorter.arr
    print("Sorted array:", sorted_array)
