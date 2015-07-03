__author__ = 'dido-ubuntu'

import unittest
import aelib.randomsampling.disk_knownsequencelen as knownSequence


class TestRandomSampling(unittest.TestCase):


    def setUp(self):
        self.n = 100
        self.sequence = [x for x in range(self.n)]
        self.m = 20

    def tearDown(self):
        self.sequence = [x for x in range(self.n)]


    def test_drawnUnsampled(self):
        gen_sampled = knownSequence.drawnUnsampled(self.sequence, self.m)
        items_sampled = [x for x in gen_sampled]
        different_items = list(set(items_sampled)) # removed possible double sampled items with the set function
        self.assertEqual(len(different_items), self.m)

    def test_drawnDictionary(self):
        gen_sampled = knownSequence.drawnDictionary(self.n, self.m)
        items_sampled = [x for x in gen_sampled]
        different_items = list(set(items_sampled)) # removed possible double sampled items with the set function
        self.assertEqual(len(different_items), self.m)