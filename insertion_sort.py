# INSERTION_SORT
# Sort a list or a numpy array.

def insertion_sort(A, n):
    """
    Argument:
    A --- a list or a numpy array
    n --- length of A
    """

    for i in range(1, n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key


# Example usage
if __name__ == '__main__':
    list1 = [31, 41, 59, 26, 41, 58]
    list1test = list(list1)
    insertion_sort(list1, len(list1))
    print(list1)
    print(list1 == sorted(list1test))
