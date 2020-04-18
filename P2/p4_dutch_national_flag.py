#!/usr/bin/env python3
"""
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

Args:
    input_list(list): List to be sorted
"""

import unittest


def sort_012(arr):
    lo = 0
    mid = 0
    hi = len(arr) - 1

    while mid <= hi:
        elem = arr[mid]
        if 0 == elem:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif 1 == elem:
            mid += 1
        elif 2 == elem:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
    return arr


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        return True
    else:
        return False


class UnitTests(unittest.TestCase):
    def test_case(self):
        self.assertTrue(test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))
        self.assertTrue(test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
        self.assertTrue(test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
        self.assertTrue(test_function([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        self.assertTrue(test_function([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertTrue(test_function([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
        self.assertTrue(test_function([]))


if __name__ == '__main__':
    print('Running UT cases:')
    unittest.main()
