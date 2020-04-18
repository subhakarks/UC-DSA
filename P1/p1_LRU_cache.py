#!/usr/bin/env python3

import unittest
from .dlinked_list import dlinked_list


class LRU_Cache(object):
    def __init__(self, capacity):
        if capacity < 1:
            raise Exception('LRU Cache: invalid cache capacity')
        self.sz = capacity
        self.q = dlinked_list()
        self.key_hash = dict()

    def get(self, key):
        if key not in self.key_hash:
            return -1

        # note: storing a tuple of (key, value) in the queue.
        node = self.key_hash[key]
        # referenced item is at head, do nothing
        if self.q.dll_is_head_node(node):
            return node.value[1]

        val = node.value  # note: value is (k, v) tuple
        self.q.dll_remove_node(node)
        self.q.dll_insert_head(val)
        return val[1]

    def set(self, key, value):
        # if key is already in cache, just refresh it
        if key in self.key_hash:
            node = self.key_hash[key]
            node.value = (key, value)  # update value if it has changed
            # if key is already at head, do nothing
            if self.q.dll_is_head_node(node):
                return
            self.q.dll_remove_node(node)
            self.q.dll_insert_head((key, value))
            return
        else:
            # key is not in cache, insert it at head
            if self.sz == len(self.key_hash):
                # cache has reached its capacity. remove least recently used key to
                # make room for new element. make sure to remove key from hash to
                # indicate that this item is no longer present in cache
                (d_key, d_value) = self.q.tail.value
                del self.key_hash[d_key]
                self.q.dll_remove_tail()
            # insert new key at head
            self.q.dll_insert_head((key, value))
            self.key_hash[key] = self.q.head
        return


class UnitTests(unittest.TestCase):
    def test_case_1(self):
        c = LRU_Cache(capacity=5)
        c.set(1, 1)
        c.set(2, 2)
        c.set(3, 3)
        c.set(4, 4)
        self.assertEqual(1, c.get(1))
        self.assertEqual(2, c.get(2))
        self.assertEqual(-1, c.get(9))
        c.set(5, 5)
        c.set(6, 6)
        self.assertEqual(-1, c.get(3))

    def test_case_2(self):
        c = LRU_Cache(capacity=5)
        self.assertEqual(-1, c.get(9))

    def test_case_3(self):
        c = LRU_Cache(capacity=1)
        c.set(1, 1)
        self.assertEqual(1, c.get(1))
        c.set(2, 2)
        self.assertEqual(-1, c.get(1))


if __name__ == '__main__':
    print("Running UT cases.......\n")
    unittest.main()
