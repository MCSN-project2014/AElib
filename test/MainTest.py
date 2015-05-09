__author__ = 'dido-ubuntu'

import unittest

from test.test_sortingAtomic import TestSortingAtomic
from test.test_datastructures import TestTrie

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortingAtomic)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestTrie)
    unittest.TextTestRunner(verbosity=2).run(suite)