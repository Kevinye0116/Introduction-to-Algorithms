# Binary_Search

def Binary_Search(arr, target):
    arr1 = arr.copy()
    sorted(arr1)
    left, right = 0, len(arr)-1

    while left <= right:
        mid = left+(right-left)//2

        if target == arr1[mid]:
            answer = arr.index(arr1[mid])
            return f"Target element found in the array with index {answer}"
        elif arr1[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return "Target Not Found!"


# Example usage
list1 = [31, 41, 59, 26, 41, 58]
target = 31
result = Binary_Search(list1, target)
print(result)
