"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""

    low_val = 0  # initialising lower value to 0
    mid_val = 0  # initialising mid value to 0
    high_val = len(
        input_array) - 1  # initialising high value to length of the list [ -1, since array indexing starts from zero]

    while low_val <= high_val:
        # to get integer result
        mid_val = (high_val + low_val) // 2

        # check is value is present at mid
        if input_array[mid_val] < value:
            low_val = mid_val + 1

        # if value is greater, compare to the right of mid
        elif input_array[mid_val] > value:
            high_val = mid_val - 1

        # if value is smaller, compared to the left of mid
        else:
            return mid_val

        # element was not present in the list, return -1

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15

print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))