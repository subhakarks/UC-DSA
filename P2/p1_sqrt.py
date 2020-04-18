#!/usr/bin/env python3
"""
Calculate the floored square root of a number

Args:
    number(int): Number to find the floored squared root
Returns:
    int: Floored Square Root
"""

import unittest


def sqrt(num):
    if num is None or num < 0:
        return 'UNSUPPORTED'

    if num in (0, 1):
        return num

    ret = 0
    start = 1
    end = num // 2
    while start <= end:
        mid = (start + end) // 2
        sq = mid * mid

        if sq == num:
            return mid
        if sq > num:
            end = mid - 1
        else:
            start = mid + 1
            ret = mid
    return ret


class UnitTests(unittest.TestCase):
    def test_case(self):
        self.assertEqual(0, sqrt(0))
        self.assertEqual(1, sqrt(1))
        self.assertEqual(1, sqrt(2))
        self.assertEqual(3, sqrt(9))
        self.assertEqual(4, sqrt(16))
        self.assertEqual(5, sqrt(25))
        self.assertEqual(5, sqrt(28))
        self.assertEqual(9, sqrt(81))
        self.assertEqual('UNSUPPORTED', sqrt(None))
        self.assertEqual('UNSUPPORTED', sqrt(-9))


if __name__ == '__main__':
    print('Running UT cases:')
    unittest.main()
