__author__ = 'dido-ubuntu'
import unittest
import aelib.datastructure.datastruct as datastruct
import aelib.utils


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.array_strings = ["abh", "aec", "bbb",  "aah", "ggg", "lbb", "lll"] # esempio  pag 6-3 notes


    def tearDown(self):
        self.array_strings = ["abh", "aec", "bbb",  "aah", "ggg", "lbb", "lll"] # esempio  pag 6-3 notes

    def test_trie(self ):
        dict_naming = aelib.utils.naming(self.array_strings)
        trie = datastruct.Trie(10, dict_naming)
        for string in self.array_strings:
            trie.insert(string)
        self.assertEqual(trie.visitInOrder(), sorted(self.array_strings))