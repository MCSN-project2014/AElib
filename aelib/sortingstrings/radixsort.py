__author__ = 'dido-ubuntu'



import aelib.utils as utils

def msd_first(listStrings):
    """
    Most Significant Digit algorithms.
     Process strings char-by-char from their beginning
    and  distributes them into sigma (size of alphabet) buckets.
    :param listStrings:
    :return:
    """

    dictNaming = utils.naming(listStrings) #dictionary {'char':rank } #takes O(N log(sigma))) N=n*L  L=length single string
    numbuckets = len(dictNaming) # number of distinct character in the strings



def lsd_first(listStrings):
    """
    Last significant Digit algorithms.
    :param listStrings:
    :return:
    """
