#!/usr/bin/env python3

import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = new_node
        return

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def get_as_list(self):
        ret = list()
        trav = self.head
        while trav:
            ret.append(trav.value)
            trav = trav.next
        return ret


def union(llist_1, llist_2):
    ret = LinkedList()
    val_hash = set()

    def _trav_llist(llist):
        trav = llist.head
        while trav:
            val = trav.value
            if val not in val_hash:
                ret.append(val)
                val_hash.add(val)
            trav = trav.next

    _trav_llist(llist=llist_1)
    _trav_llist(llist=llist_2)
    return ret


def intersection(llist_1, llist_2):
    ret = LinkedList()
    l1_val_hash = set()
    trav = llist_1.head
    while trav:
        l1_val_hash.add(trav.value)
        trav = trav.next

    trav = llist_2.head
    already_added_hash = set()
    while trav:
        val = trav.value
        if val in l1_val_hash:
            if val not in already_added_hash:
                ret.append(val)
                already_added_hash.add(val)
        trav = trav.next
    return ret


class UnitTests(unittest.TestCase):
    def base_test(self, arr1, arr2):
        list1 = LinkedList()
        list2 = LinkedList()
        for i in arr1:
            list1.append(i)
        for i in arr2:
            list2.append(i)
        u_list = union(list1, list2)
        i_list = intersection(list1, list2)
        ret_u_list = sorted(u_list.get_as_list())
        ret_i_list = sorted(i_list.get_as_list())
        s1 = set(arr1)
        s2 = set(arr2)
        u_set = s1.union(s2)
        i_set = s1.intersection(s2)
        cmp_u_list = sorted(u_set)
        cmp_i_list = sorted(i_set)
        self.assertEqual(ret_u_list, cmp_u_list)
        self.assertEqual(ret_i_list, cmp_i_list)

    def test_case1(self):
        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
        element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
        self.base_test(element_1, element_2)

    def test_case2(self):
        element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
        element_2 = [1, 7, 8, 9, 11, 21, 1]
        self.base_test(element_1, element_2)

    def test_case3(self):
        arr1 = [1, 1]
        arr2 = [2, 2]
        self.base_test(arr1, arr2)
        self.base_test([], [2])
        self.base_test([9], [])


if __name__ == '__main__':
    print('Running UT cases:')
    unittest.main()
