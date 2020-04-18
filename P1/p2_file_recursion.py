#!/usr/bin/env python3

import os
import unittest


def find_files(suffix, path):
    if not path or not suffix:
        return []
    ret_paths = list()
    dir_list = os.listdir(path)
    for entry in dir_list:
        entry = os.path.join(path, entry)
        if os.path.isfile(entry) and entry.endswith(suffix):
            ret_paths.append(entry)
        elif os.path.isdir(entry):
            ret_paths.extend(find_files(suffix, entry))
    return ret_paths


class UnitTests(unittest.TestCase):
    def test_case(self):
        out = [
            './testdir/subdir3/subsubdir1/b.c',
            './testdir/t1.c',
            './testdir/subdir5/a.c',
            './testdir/subdir1/a.c'
        ]
        self.assertEqual(out, find_files('.c', './testdir'))
        self.assertEqual([], find_files('.py', './testdir'))
        self.assertEqual(4, len(find_files('.h', './testdir')))

    def test_case2(self):
        self.assertEqual([], find_files('', ''))
        self.assertEqual([], find_files('.c', ''))
        self.assertEqual([], find_files('', './testdir'))


if __name__ == '__main__':
    print('Running UT cases:')
    unittest.main()
