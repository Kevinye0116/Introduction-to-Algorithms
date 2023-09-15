class Heap_Sort:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def max_heapify(self, i):
        largest = i
        l = self.left(i)
        r = self.right(i)

        if l < self.n and self.arr[l] > self.arr[largest]:
            largest = l

        if r < self.n and self.arr[r] > self.arr[largest]:
            largest = r

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        for i in range(self.n // 2 - 1, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(self.n - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.n -= 1
            self.max_heapify(0)


# Example Usage
if __name__ == "__main__":
    input_array = [4, 10, 3, 5, 1]
    s = Heap_Sort(input_array)
    s.heap_sort()
    print(s.arr)
