
from SortingAtomic import SnowPlow
from SortingAtomic import MergeSort
from SortingAtomic import _threePartition
from SortingAtomic import QuickSort
import unittest



class testSortingAtomic(unittest.TestCase):


    """
    def test_snowPlow(self):
        s = [2,5,4,7,1,4,2]
        for i in range(sizeM):
            u.append(s.pop(0))
        snowPlowPhase(u)
        self.assertEqual(mergeSort(A),[1,2,3,5,7,9])
        self.assertEqual()
    """

    def test_threePartition(self):
        s  =[9,8,7,6,5,4,3,2,1]
        #s = [1,2,3,4,5,6,7,9]
        indexes = _threePartition(s,0,len(s)-1)
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

    def test_quickSort(self):
        s = [9,8,7,6,5,4,3,2,1,0]
        test = s[:]
        test.sort()
        QuickSort( s , 0 , len(s)-1)
        self.assertEqual( s , test )

    def test_mergeSort(self):
        s = [9,8,7,6]
        test = s[:]
        test.sort()
        MergeSort( s, 1, len(s) )
        self.assertEqual( s , test )


suite = unittest.TestLoader().loadTestsFromTestCase(testSortingAtomic)
unittest.TextTestRunner(verbosity=2).run(suite)
