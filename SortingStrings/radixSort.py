
import datastruct
import utils

__author__ = 'dido-ubuntu'




def msd(listStrings):
    """
    Most Significant Digit algorithms.
     Process strings char-by-char from their beginning
    and  distributes them into sigma (size of alphabet) buckets.

    :param listStrings:
    :return:
    """

    dictNaming = utils.naming(listStrings) #dictionary {'char':rank } #takes O(N log(sigma))) N=n*L  L=length single string
    numbuckets = len(dictNaming)






