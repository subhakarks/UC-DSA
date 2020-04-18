#!/usr/bin/env python3

import unittest


class RouteTrieNode:
    def __init__(self):
        self.paths = {}
        self.handler = None

    def insert(self, path):
        if path not in self.paths:
            self.paths[path] = RouteTrieNode()


class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()

    def _split_path(self, path):
        subs = path.split('/')
        if '' == subs[0]:
            subs[0] = '/'
        if '' == subs[-1]:
            subs.pop(-1)
        return subs

    def insert(self, path, handler):
        subs = self._split_path(path)
        trav = self.root
        handler = handler or 'Handler Not Defined'
        for elem in subs:
            trav.insert(elem)
            trav = trav.paths[elem]
        trav.handler = handler

    def find(self, path):
        subs = self._split_path(path)
        trav = self.root
        for elem in subs:
            if elem not in trav.paths:
                return None
            trav = trav.paths[elem]
        return trav.handler


class Router:
    def __init__(self, root_path, root_handler):
        self.trie = RouteTrie()
        self.trie.insert(root_path, root_handler)

    def add_handler(self, path, handler=None):
        self.trie.insert(path, handler)

    def lookup(self, path):
        return self.trie.find(path)


class UnitTests(unittest.TestCase):
    def test_case(self):
        router = Router('/', 'Root Handler')
        router.add_handler('/home/about', 'About Handler')
        router.add_handler('/home/me')
        self.assertEqual(router.lookup('/'), 'Root Handler')
        self.assertEqual(router.lookup('/home'), None)
        self.assertEqual(router.lookup('/home/about'), 'About Handler')
        self.assertEqual(router.lookup('/home/about/'), 'About Handler')
        self.assertEqual(router.lookup('/home/about/me'), None)
        self.assertEqual(router.lookup('/home/me'), 'Handler Not Defined')


if __name__ == '__main__':
    print('Running UT cases:')
    unittest.main()
