import unittest
import random

import aelib.sortingatomic.distr_based as dtrBased
import aelib.sortingatomic.merge_based as mrgBased
import aelib.sortingstrings.radixsort as rdxsort


class TestSortingAtomic(unittest.TestCase):

    def setUp(self):
        self.reverse_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.arrayStrings = ["zzz", "zaz", "bbb", "bab", "cac", "ccc", "dav", "ddc"]
        self.random_array = [random.randint(1, 10) for i in range(10)]

    def tearDown(self):
        self.reverse_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        self.arrayStrings = ["zzz", "zaz", "bbb", "bab", "cac", "ccc", "dav", "ddc"]
        self.random_array = [random.randint(1, 10) for i in range(10)]

    def test_quickSort(self):
        dtrBased.quicksort(self.random_array, 0, len(self.random_array) - 1)
        dtrBased.quicksort(self.reverse_array, 0, len(self.reverse_array) - 1)
        self.assertEqual(self.random_array, sorted(self.random_array))
        self.assertEqual(self.reverse_array, sorted(self.reverse_array))

    def test_mergeSort(self):
        sorted_rev_array = mrgBased.mergesort(self.reverse_array)
        sorted_rand_array = mrgBased.mergesort(self.random_array)
        self.assertEqual(sorted_rev_array, sorted(self.reverse_array))
        self.assertEqual(sorted_rand_array, sorted(self.random_array))

    def test_trie(self):
        msdsorted = rdxsort.msd_first(self.arrayStrings)
        self.assertEqual(msdsorted, sorted(self.arrayStrings))

    """
    def test_snowPlow(self):
        s = [2,5,4,7,1,4,2]
        for i in range(sizeM):
            u.append(s.pop(0))
        snowPlowPhase(u)
        self.assertEqual(mergeSort(A),[1,2,3,5,7,9])
        self.assertEqual()


    def test_threePartition(self):
        s  =[9,8,7,6,5,4,3,2,1]
        #s = [1,2,3,4,5,6,7,9]
        indexes = dtrBased._threePartition(s,0,len(s)-1)
        l = indexes[0]
        r = indexes[1]
        p = s[l]
        for k in range(0, len(s)-1):
            if( k < l):
                self.assertLess(s[k], p)
            elif( k >= l and k <= r):
                self.assertEqual( s[k] , p)
            elif( k > r and k < len(s)):
                self.assertGreater(s[k], p)


    """
