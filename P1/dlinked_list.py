#!/usr/bin/env python3

import unittest


class dll_node(object):
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


class dlinked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def dll_as_list(self):
        ret = list()
        trav = self.head
        while trav:
            ret.append(trav.value)
            trav = trav.next
        return ret

    def dll_is_head_node(self, node):
        return node == self.head

    def dll_insert_head(self, value):
        node = dll_node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.head.prev = node
        node.next = self.head
        self.head = node
        return

    def dll_insert_tail(self, value):
        node = dll_node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        return

    def dll_remove_head(self):
        # empty list
        if self.head is None:
            return
        # list has only one node
        if self.head.next is None:
            self.head = self.tail = None
            return
        nxt = self.head.next
        nxt.prev = None
        self.head = nxt
        return

    def dll_remove_tail(self):
        # empty list
        if self.tail is None:
            return
        # list has only one node
        if self.tail.prev is None:
            self.head = self.tail = None
            return
        prev = self.tail.prev
        prev.next = None
        self.tail = prev
        return

    def dll_remove_node(self, node):
        if node is None:
            return
        if node == self.head:
            return self.dll_remove_head()
        if node == self.tail:
            return self.dll_remove_tail()
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        return


class UnitTests(unittest.TestCase):
    def test_case_1(self):
        dll = dlinked_list()
        self.assertEqual([], dll.dll_as_list())
        dll.dll_insert_tail(9)
        self.assertEqual([9], dll.dll_as_list())
        dll.dll_remove_head()
        self.assertEqual([], dll.dll_as_list())
        dll.dll_remove_head()
        self.assertEqual([], dll.dll_as_list())
        dll.dll_remove_tail()
        self.assertEqual([], dll.dll_as_list())
        dll.dll_insert_tail(9)
        dll.dll_remove_tail()
        self.assertEqual([], dll.dll_as_list())
        dll.dll_remove_tail()
        self.assertEqual([], dll.dll_as_list())
        dll.dll_remove_head()
        self.assertEqual([], dll.dll_as_list())

    def test_case_2(self):
        dll = dlinked_list()
        dll.dll_insert_tail(9)
        dll.dll_insert_head(8)
        self.assertEqual([8, 9], dll.dll_as_list())
        dll.dll_remove_tail()
        self.assertEqual([8], dll.dll_as_list())
        dll.dll_remove_tail()
        self.assertEqual([], dll.dll_as_list())
        dll.dll_insert_tail(9)
        dll.dll_insert_head(8)
        dll.dll_remove_head()
        self.assertEqual([9], dll.dll_as_list())
        dll.dll_remove_head()
        self.assertEqual([], dll.dll_as_list())

    def test_case_3(self):
        dll = dlinked_list()
        dll.dll_insert_tail(9)
        dll.dll_insert_head(8)
        dll.dll_remove_node(dll.head)
        self.assertEqual([9], dll.dll_as_list())
        dll.dll_remove_node(dll.head)
        self.assertEqual([], dll.dll_as_list())
        dll.dll_insert_tail(9)
        dll.dll_insert_head(8)
        self.assertEqual([8, 9], dll.dll_as_list())
        dll.dll_remove_node(dll.tail)
        self.assertEqual([8], dll.dll_as_list())
        dll.dll_remove_node(dll.tail)
        self.assertEqual([], dll.dll_as_list())

    def test_case_4(self):
        dll = dlinked_list()
        dll.dll_insert_tail(9)
        dll.dll_insert_head(8)
        dll.dll_insert_tail(10)
        self.assertEqual([8, 9, 10], dll.dll_as_list())
        dll.dll_remove_node(dll.head.next)
        self.assertEqual([8, 10], dll.dll_as_list())
        dll.dll_remove_node(dll.tail.prev)
        self.assertEqual([10], dll.dll_as_list())


if __name__ == '__main__':
    print("Running UT cases.......\n")
    unittest.main()
