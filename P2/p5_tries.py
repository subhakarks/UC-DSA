#!/usr/bin/env python3
import unittest


class TrieNode:
    def __init__(self):
        self.chars = {}
        self.last = False

    def insert(self, char):
        if char not in self.chars:
            self.chars[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        if not len(self.chars):
            return []
        ret = []
        for ch, t_node in self.chars.items():
            if t_node.last:
                ret.append(suffix + ch)
            ret.extend(t_node.suffixes(suffix + ch))
        return ret


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        trav = self.root
        for char in word:
            trav.insert(char)
            trav = trav.chars[char]
        trav.last = True

    def find(self, prefix):
        trav = self.root
        for char in prefix:
            if char not in trav.chars:
                return None
            trav = trav.chars[char]
        return trav


class UnitTests(unittest.TestCase):
    def test_case(self):
        trie = Trie()
        wordList = [
            "ant", "anthology", "antagonist", "antonym",
            "fun", "function", "factory",
            "trie", "trigger", "trigonometry", "tripod"
        ]
        for word in wordList:
            trie.insert(word)
        self.assertEqual(['hology', 'agonist', 'onym'],
                         trie.find('ant').suffixes())
        self.assertEqual(['ction'],
                         trie.find('fun').suffixes())


if __name__ == '__main__':
    print('Running UT cases:')
    unittest.main()
