__author__ = 'dido-ubuntu'

import random
import aelib.utils as utils
import aelib.dictionaryproblem.dp_datastruct as Dictionary


def drawnUnsampled(sequence, m):
    """
     Algorithm 3.1 of the notes
    :param sequence: the list of items to be select uniformly at random
    :param m: the number of items to be select (m < len(sequence))
    :return: return a generator for the sampled items
    """
    copySequence = list(sequence) #copy the sequence
    n = len(copySequence)
    for s in range(0, m):
        p = random.randint(0, (n-1)-s)
        item = copySequence[p]
        utils.swap(copySequence, p, (n-1)-s)
        yield item


def drawnDictionary(n, m):
    """
    Algorithm 3.2 of the notes.
    It uses a dictionary implemented as hash table with chaining: this keeps track of the selected items in sorted order,
    and needs only O(m) space.

    :param n: total number of positions
    :param m: the amount of positions to be selected
    :return: Return a generator of m distinct integer which constitute the positions of the items to be sampled
    """
    dictionary = Dictionary.HashTable(m, lambda x: x % m)
    while len(dictionary) != m:
        p = random.randint(0, (n-1))
        if dictionary.search(p) is None:
            dictionary.insert(p)
            yield p


