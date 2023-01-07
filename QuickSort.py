"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    less = []  # list to handle numbers lesser than the pivot
    equal = []  # list to handle the number == pivor
    greater = []  # list to handle the number greater than the pivot

    if len(array) > 1:
        pivot = array[0]  # choosing the first element as the pivot
        for x in array:  # iterating over every element in the array
            if x < pivot:
                less.append(x)  # lesser numbers appends in the less list
            elif x == pivot:
                equal.append(x)  # the pivot appends in the equal list
            elif x > pivot:
                greater.append(x)  # greater number appends in the greater list

        # using recursion  + using '+'  operator to join the lists together
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))