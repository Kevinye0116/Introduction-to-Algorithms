class BucketSort:
    def sort(self, arr):
        if len(arr) == 0:
            return arr

        min_value = min(arr)
        max_value = max(arr)

        num_buckets = len(arr)

        buckets = [[] for _ in range(num_buckets)]

        for num in arr:
            index = int((num - min_value) / (max_value - min_value) * (num_buckets - 1))
            buckets[index].append(num)

        for bucket in buckets:
            bucket.sort()

        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(bucket)

        return sorted_arr


# Example Test
s = BucketSort()
arr = [0.42, 0.32, 0.75, 0.12, 0.89, 0.11, 0.33]
sorted_arr = s.sort(arr)
print(sorted_arr)
