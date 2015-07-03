__author__ = 'dido-ubuntu'

import unittest

from test.test_sortingAtomic import TestSortingAtomic
from test.test_datastructures import TestTrie
from test.test_prefixsearch import TestPrefixSearch
from test.test_randomsampling import TestRandomSampling

if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortingStrings)
    unittest.TextTestRunner(verbosity=2).run(suite)
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTrie)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestPrefixSearch)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestRandomSampling)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortingAtomic)
    unittest.TextTestRunner(verbosity=2).run(suite)
    """