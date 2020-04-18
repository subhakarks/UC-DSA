#!/usr/bin/env python3
"""
Rearrange Array Elements so as to form two number such that their sum is maximum.

Args:
    input_list(list): Input List
Returns:
    (int),(int): Two maximum sums
"""
import unittest


def merge_sorted_lists(left, right):
    l_idx = 0
    r_idx = 0
    merged = []
    while (l_idx < len(left) and r_idx < len(right)):
        if left[l_idx] >= right[r_idx]:
            merged.append(left[l_idx])
            l_idx += 1
        else:
            merged.append(right[r_idx])
            r_idx += 1

    merged += left[l_idx:]
    merged += right[r_idx:]
    return merged


def merge_sort_r(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort_r(arr[:mid])
    right = merge_sort_r(arr[mid:])
    return merge_sorted_lists(left, right)


def rearrange_digits(arr):
    sz = len(arr)
    if sz < 2:
        return []

    s_arr = merge_sort_r(arr)
    if 2 == sz:
        return s_arr

    n1 = 0
    n2 = 0
    for i in range(0, (sz - 1), 2):
        n1 = (n1 * 10) + s_arr[i]
        n2 = (n2 * 10) + s_arr[i + 1]

    if sz % 2:  # odd-sized array
        n1 = (n1 * 10) + s_arr[sz - 1]
    return [n1, n2]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        return True
    else:
        return False


class UnitTests(unittest.TestCase):
    def test_case(self):
        self.assertTrue(test_function(([], [])))
        self.assertTrue(test_function(([9], [])))
        self.assertTrue(test_function(([8, 9], [9, 8])))
        self.assertTrue(test_function(([8, 6, 9], [98, 6])))
        self.assertTrue(test_function(([1, 2, 3, 4, 5], [542, 31])))
        self.assertTrue(test_function(([4, 6, 2, 5, 9, 8], [964, 852])))


if __name__ == '__main__':
    print('Running UT cases:')
    unittest.main()
