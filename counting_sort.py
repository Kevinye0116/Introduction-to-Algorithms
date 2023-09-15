#####################################################
# COUNTING SORT IS SUITABLE FOR SCENARIOS WHERE THE #
# RANGE OF ELEMENTS IN THE ARRAY TO BE SORTED IS    #
# RELATIVELY SMALL AND IS ONLY FOR NON-NEGETIVE INT #
#####################################################


class CountingSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        min_value = min(self.arr)
        max_value = max(self.arr)
        range_of_elements = max_value - min_value + 1

        counting_arr = [0] * range_of_elements

        for num in self.arr:
            counting_arr[num - min_value] += 1

        for i in range(1, len(counting_arr)):
            counting_arr[i] += counting_arr[i - 1]

        sorted_arr = [0] * len(self.arr)
        for num in self.arr:
            sorted_arr[counting_arr[num - min_value] - 1] = num
            counting_arr[num - min_value] -= 1

        return sorted_arr


# Example Test

arr = [2, 5, 3, 0, 2, 3, 0, 3]
s = CountingSort(arr)
answer = s.sort()
print(answer)
