#!/usr/bin/env python3

"""
Find the index by searching in a rotated sorted array

Args:
input_list(array), number(int): Input array to search and the target

Returns:
int: Index or -1
"""
import unittest


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def seach_pivot(arr, lo, hi):
    if lo > hi:
        return -1
    if lo == hi:
        return lo

    mid = (lo + hi) // 2
    if arr[mid] > arr[mid + 1]:
        return mid

    if arr[mid] < arr[mid - 1]:
        return mid - 1

    if arr[lo] > arr[mid]:
        return seach_pivot(arr, lo, mid - 1)

    return seach_pivot(arr, mid + 1, hi)


def binary_search(arr, lo, hi, num):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if num == arr[mid]:
        return mid
    if num < arr[mid]:
        return binary_search(arr, lo, mid - 1, num)
    return binary_search(arr, mid + 1, hi, num)


def rotated_array_search(input_list, number):
    sz = len(input_list)

    if not sz:
        return -1

    # given array is not rotated afterall
    if input_list[0] < input_list[-1]:
        return binary_search(input_list, 0, sz - 1, number)

    # given list is rotated at a random pivot
    pivot = seach_pivot(input_list, 0, sz - 1)

    if number == input_list[pivot]:
        return pivot

    if number < input_list[0]:
        return binary_search(input_list, pivot + 1, sz - 1, number)

    return binary_search(input_list, 0, pivot - 1, number)


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        return True
    return False


class UnitTests(unittest.TestCase):
    def test_case(self):
        self.assertTrue(test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]))
        self.assertTrue(test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]))
        self.assertTrue(test_function([[6, 7, 8, 1, 2, 3, 4], 8]))
        self.assertTrue(test_function([[6, 7, 8, 1, 2, 3, 4], 1]))
        self.assertTrue(test_function([[6, 7, 8, 1, 2, 3, 4], 10]))
        self.assertTrue(test_function([[9], 10]))
        self.assertTrue(test_function([[], 10]))


if __name__ == '__main__':
    print('Running UT cases:')
    unittest.main()
