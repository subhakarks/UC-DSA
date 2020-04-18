#!/usr/bin/env python3

import time
import hashlib
import unittest


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.data = data
        self.next = None
        self.timestamp = timestamp
        self.hash = self.calc_hash(data)
        self.previous_hash = previous_hash

    def calc_hash(self, data):
        sha = hashlib.sha256()
        data = str(data)
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_hash(self):
        return self.hash

    def get_previous_hash(self):
        return self.previous_hash


class BlockChain:
    def __init__(self):
        self.bc_head = None
        self.bc_tail = None
        self.last_hash = None

    def add_block(self, data):
        ts = time.strftime('%H:%M %m/%d/%Y', time.gmtime())
        new_block = Block(timestamp=ts, data=data, previous_hash=self.last_hash)
        self.last_hash = new_block.get_hash()
        if self.bc_tail is None:
            self.bc_head = self.bc_tail = new_block
        else:
            self.bc_tail.next = new_block
            self.bc_tail = self.bc_tail.next
        return

    def get_block_chain(self):
        ret = list()
        trav = self.bc_head
        while trav:
            ret.append(trav)
            trav = trav.next
        return ret


class UnitTests(unittest.TestCase):
    def test_case_1(self):
        bc = BlockChain()
        self.assertEqual(0, len(bc.get_block_chain()))

    def test_case_2(self):
        bc = BlockChain()
        bc.add_block('data-1')
        bc.add_block('data-2')
        bc.add_block('data-3')
        ret = bc.get_block_chain()
        self.assertEqual(3, len(ret))


if __name__ == '__main__':
    print("Running UT cases.......\n")
    unittest.main()
