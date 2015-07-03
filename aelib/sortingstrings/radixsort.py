__author__ = 'dido-ubuntu'



import aelib.utils as utils
import aelib.sortingstrings.ss_datastruct as sortStringsStruct

def msd_first(listStrings):
    """
    Most Significant Digit algorithms.
    Process strings char-by-char from their beginning
    and  distributes them into sigma (size of alphabet) buckets.
    :param listStrings: a list of strings.
    :return:
    """

    dictNaming = utils.naming(listStrings)      #dictionary {'char':rank } #takes O(N log(sigma))) N=n*L  L=length single string
    sigma = len(dictNaming)                     # number of distinct character in the strings

    trie = sortStringsStruct.TrieArray(sigma, dictNaming)
    for string in listStrings:
        trie.insert(string)

    return trie.visitInOrder()

def lsd_first(listStrings):
    """
    Last significant Digit algorithms.
    :param listStrings:
    :return:
    """
