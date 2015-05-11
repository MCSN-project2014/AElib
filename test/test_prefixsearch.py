__author__ = 'dido-ubuntu'
import unittest

import  aelib.prefixsearch.frontcoding as frontcoding




class TestPrefixSearch(unittest.TestCase):

    def setUp(self):
        self.dict_strings = {0: "alcatraz", 1: "alcool", 2: "alcyone", 3:"anacleto", 4:"ananas",5:"aster",6:"astral",7:"astronomy"} # esempio  pag 7-4 notes


    #def tearDown(self):
        #self.array_strings = ["abh", "aec", "bbb",  "aah", "ggg", "lbb", "lll"] # esempio  pag 6-3 notes

    def test_frontcoding(self):
        compressed = frontcoding.front_coding(self.dict_strings)
        result = [(0, "alcatraz"), (3, "ool"), (3, "yone"), (1, "nacleto"), (3, "nas"), (1, "ster"), (3, "ral"), (4, "onomy")]
        self.assertEqual(result, compressed)