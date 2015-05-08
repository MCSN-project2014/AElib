__author__ = 'dido-ubuntu'

import unittest

from test.test_sortingAtomic import TestSortingAtomic


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortingAtomic)
    unittest.TextTestRunner(verbosity=2).run(suite)
