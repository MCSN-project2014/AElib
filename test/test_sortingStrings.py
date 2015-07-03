import unittest
import random


from aelib.sortingstrings.ss_datastruct import countingSort as countingSort


class TestSortingStrings(unittest.TestCase):

    def setUp(self):
        self.reverse_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        #self.arrayStrings = ["zzz", "zaz", "bbb", "bab", "cac", "ccc", "dav", "ddc"]
        #self.random_array = [random.randint(1, 10) for i in range(10)]

    def test_countingSort(self):
        k = 10
        s = [random.randint(1, k) for i in range(50)]
        self.assertEqual(countingSort(s, k), sorted(s))

