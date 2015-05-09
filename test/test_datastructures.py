__author__ = 'dido-ubuntu'
import unittest
import aelib.datastructure.datastruct as datastruct
import aelib.utils


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.array_strings = ["abh", "aec", "bbb",  "aah", "ggg", "lbb", "lll"] # esempio  pag 6-3 notes


    def tearDown(self):
        self.reverse_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


    def test_trie(self ):
        dict_naming = aelib.utils.naming(self.array_strings)
        trie = datastruct.Trie(10, dict_naming)
        for string in self.array_strings:
            trie.insert(string)
        print(trie)