# Maximum Subarray Question
# Divide and Conquer Algorithm

class Maximum_Subarray:
    def __init__(self, arr):
        self.arr = arr

    def find_max_crossing_subarray(self, low, mid, high):
        left_sum = float('-inf')
        max_left = mid
        sum = 0
        for i in range(mid, low - 1, -1):
            sum += self.arr[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i

        right_sum = float('-inf')
        max_right = mid + 1
        sum = 0
        for j in range(mid + 1, high + 1):
            sum += self.arr[j]
            if sum > right_sum:
                right_sum = sum
                max_right = j

        return max_left, max_right, left_sum+right_sum

    def find_max_subarray(self, low, high):

        if low == high:
            return low, high, self.arr[low]

        mid = (low + high) // 2
        left_low, left_high, left_sum = self.find_max_subarray(low, mid)
        right_low, right_high, right_sum = self.find_max_subarray(
            mid + 1, high)
        cross_low, cross_high, cross_sum = self.find_max_crossing_subarray(
            low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

    def max_subarray(self):
        low, high, max_sum = self.find_max_subarray(0, len(self.arr) - 1)
        return self.arr[low:high+1], max_sum


arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
s = Maximum_Subarray(arr)
result_subarray, result_sum = s.max_subarray()
print(result_subarray, result_sum)
