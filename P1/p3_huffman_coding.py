#!/usr/bin/env python3

import unittest
from collections import defaultdict


class mh_node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.rite = None


class huffman_codec:
    def __init__(self, data):
        self.h_sz = 0
        self.heap = None
        self.data = data
        self.hf_codes = None
        self.encode_data()

    def encode_data(self):
        char_freq = defaultdict(int)
        for c in self.data:
            char_freq[c] += 1
        char_freq = sorted(char_freq.items())
        self.hf_codes = dict()
        self.h_sz = len(char_freq)
        self.heap = [mh_node(cf[0], cf[1]) for cf in char_freq]
        if 1 == len(self.heap):
            # there is only one char in the input string
            self.hf_codes[self.data[0]] = '1'
            return
        self._build_min_heap()
        self._build_huffman_tree()
        self._build_huffman_codes()

    def get_huffman_tree(self):
        return self.heap[0]

    def get_huffman_codes(self):
        return self.hf_codes

    def get_encoded_data(self):
        out = ''
        for c in self.data:
            out += self.hf_codes[c]
        return out

    def get_decoded_data(self, enc_data):
        out = ''
        trav = self.heap[0]
        for c in enc_data:
            if '0' == c:
                trav = trav.left
            else:
                trav = trav.rite
            if self._is_leaf(trav):
                out += trav.char
                trav = self.heap[0]
        return out

    def print_huffman_codes(self):
        for k, v in self.hf_codes.items():
            print('{} ---> {}'.format(k, v))
        return

    def _build_min_heap(self):
        idx = (self.h_sz - 1) // 2
        while idx > 0:
            self._shift_down(idx)
            idx -= 1
        return

    def _build_huffman_tree(self):
        while self.h_sz > 1:
            min1 = self._min_heap_extract()
            min2 = self._min_heap_extract()
            internal = mh_node('#', min1.freq + min2.freq)
            internal.left = min1
            internal.rite = min2
            self._min_heap_insert(internal)
        return

    def _build_huffman_codes(self):
        def _get_code(arr, top):
            code = []
            for i in range(0, top):
                code.append(str(arr[i]))
            return ''.join(code)

        def _build_codes(root, arr, top):
            if root.left:
                arr[top] = 0
                _build_codes(root.left, arr, top + 1)
            if root.rite:
                arr[top] = 1
                _build_codes(root.rite, arr, top + 1)
            if self._is_leaf(root):
                self.hf_codes[root.char] = _get_code(arr, top)

        top = 0
        arr = [None] * 100
        root = self.heap[0]
        _build_codes(root, arr, top)
        return

    def _min_heap_insert(self, node):
        self.heap.append(node)
        self.h_sz += 1
        parent_idx = self._parent_idx(self.h_sz - 1)
        if self._value_at(parent_idx) > self._value_at(self.h_sz - 1):
            self._shift_up(self.h_sz - 1)
        return

    def _min_heap_extract(self):
        ret = self.heap[0]
        self.heap[0] = self.heap[self.h_sz - 1]
        self.heap.pop()
        self.h_sz -= 1
        self._shift_down(0)
        return ret

    def _shift_up(self, idx):
        # while item at parent idx is greater than item and current idx,
        # move current item up and bring down parent item.
        parent_idx = self._parent_idx(idx)
        while parent_idx > 0:
            if self._value_at(parent_idx) > self._value_at(idx):
                self._swap_two_at(parent_idx, idx)
                parent_idx = self._parent_idx(parent_idx)
            else:
                break
        return

    def _shift_down(self, idx):
        # while the node at idx has a left child (and right child), do this;
        # see if any of its children are smaller than itself and if so push
        # this node and bring-up the smaller child.
        while self._lchild_idx(idx) < self.h_sz:
            # check if also has a right child.
            # if so, consider the minimum of both children
            lc_idx = self._lchild_idx(idx)
            rc_idx = self._rchild_idx(idx)
            if rc_idx < self.h_sz:
                min_child_idx = lc_idx if self._value_at(lc_idx) < self._value_at(rc_idx) else rc_idx
            else:
                min_child_idx = lc_idx
            if self._value_at(idx) > self._value_at(min_child_idx):
                self._swap_nodes_at(idx, min_child_idx)
                idx = min_child_idx
            else:
                break
        return

    def _parent_idx(self, x):
        return x // 2

    def _lchild_idx(self, x):
        return 2 * x

    def _rchild_idx(self, x):
        return (2 * x) + 1

    def _value_at(self, x):
        return self.heap[x].freq

    def _is_leaf(self, node):
        return True if (node.left is None and node.rite is None) else False

    def _swap_nodes_at(self, idx1, idx2):
        (self.heap[idx1], self.heap[idx2]) = (self.heap[idx2], self.heap[idx1])
        return


def huffman_encoding(data):
    if not data:
        return '', None
    hf_tree = huffman_codec(data)
    hf_root = hf_tree.get_huffman_tree()
    encoded_data = hf_tree.get_encoded_data()
    return encoded_data, hf_root


def huffman_decoding(encoded_data, hf_root):
    if not encoded_data or not hf_root:
        return ''
    out = ''
    trav = hf_root
    if trav.left is None and trav.rite is None:
        for c in encoded_data:
            out += trav.char
        return out
    for c in encoded_data:
        if '0' == c:
            trav = trav.left
        else:
            trav = trav.rite
        if trav.left is None and trav.rite is None:
            out += trav.char
            trav = hf_root
    return out


class UnitTests(unittest.TestCase):
    def _base_test(self, data):
        enc_data, hf_root = huffman_encoding(data)
        dec_data = huffman_decoding(enc_data, hf_root)
        self.assertEqual(data, dec_data)

    def test_case_1(self):
        self._base_test('The bird is the word')

    def test_case_2(self):
        self._base_test('9')
        self._base_test('99')
        self._base_test('99999')
        self._base_test('998899')

    def test_case_3(self):
        self._base_test('')


if __name__ == '__main__':
    print("Running UT cases.......\n")
    unittest.main()
