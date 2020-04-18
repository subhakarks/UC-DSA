#!/usr/bin/env python3
"""
Return a tuple(min, max) out of list of unsorted integers.

Args:
    ints(list): list of integers containing one or more integer
"""
import random
import unittest


def get_min_max(arr):
    if not len(arr):
        return (None, None)

    mi = arr[0]
    mx = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < mi:
            mi = arr[i]
        if arr[i] > mx:
            mx = arr[i]

    return(mi, mx)


def test_function(arr):
    (mi, mx) = get_min_max(arr)
    if not len(arr):
        return True if (None, None) == (mi, mx) else False

    if mi == min(arr) and mx == max(arr):
        return True
    else:
        return False


def generate_random_list(n_size=999, n_min=0, n_max=9999999):
    ret_set = set()
    random.seed()
    while len(ret_set) < n_size:
        ret_set.add(random.randint(n_min, n_max))
    ret = list(ret_set)
    random.shuffle(ret)
    return ret


class UnitTests(unittest.TestCase):
    def test_case(self):
        self.assertTrue(test_function([]))
        self.assertTrue(test_function([9]))
        self.assertTrue(test_function([9, 9]))
        self.assertTrue(test_function([8, 9]))
        self.assertTrue(test_function(generate_random_list()))
        self.assertTrue(test_function(generate_random_list(n_size=999999)))


if __name__ == '__main__':
    print('Running UT cases:')
    unittest.main()
