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


    def test_snowPlow(self):
        s = [5, 1, 3, 6, 2, 4, 10, 0]
        snowplow = mrgBased.SnowPlow(s, 3)
        sorted_runs = snowplow.createRuns()
        self.assertEqual(sorted_runs[0],[1,3,5,6,10])

    def test_randomSelect(self):
        s  = [1, 3, 5, 1, 2, 3, 7, 8, 6, 8, 0, 4, 10, 9] # 14 numbers [ 0,1,1,2,3,3,  4,5,6,7,8,8,9,10]
        kitem = dtrBased.randSelect(s, 5)  # k = n/2 median of the entire sequence
        self.assertEqual(kitem,3)

    """
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
