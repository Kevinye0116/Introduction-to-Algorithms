# Kadane's Algorithm


def max_subarray(nums):
    if not nums:
        return []

    max_sum = current_sum = nums[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return nums[start : end + 1]


# Example Test
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_subarray = max_subarray(nums)
print("Maximum Subarray:", result_subarray)
