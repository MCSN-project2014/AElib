
import heapq
import random
import aelib.utils as utils


def quicksort(seq, i, j):
    """
    l = index[0]
    r = index[1]
    s[l,...r] == pivot selected
    """
    if i < j:
        r = random.randint(i, j)  # pivot position selection
        utils.swap(seq, r, i)
        index = _threepartition(seq, i, j)
        quicksort(seq, i, index[0] - 1)
        quicksort(seq, index[1] + 1, j)

def _threepartition(seq, i, j):
    """
    S[i] contains the pivot.
    If the sequence scanned id S[ i , c-1]:
    S[ i , ... , l-1 ] < P
    S[ l , ... , r-1 ] = P
    S[ r , ... , c-1 ] > P

    Return vector I of the central sub-array containig all the equal items
    """
    ret = []
    P = seq[i]
    l = i
    r = i+1
    for c in range(r, j+1):
        if seq[c] == P:
            utils.swap(seq, c, r)
            r += 1
        elif seq[c] < P:
            utils.swap(seq, c, l)
            utils.swap(seq, c, r)
            l += 1
            r += 1
    ret = [l, r-1]
    return ret




def randSelect(S , k):
    """
    Randomized algorithm that select the item of the unordered S having rank k
    :param S:
    :param k:
    :return:
    """
    less, greater, equal = [], [], []
    num_less, num_greater, num_equal = 0, 0, 0
    r = random.randint(0, len(S)-1)
    for item in S:
        if item < S[r]:
            less.append(item)
            num_less += 1
        elif item == S[r]:
            equal.append(item)
            num_equal += 1
        else:
            greater.append(item)
            num_greater += 1
    if k < num_less:
        return randSelect(less, k)
    elif k < (num_less + num_equal):
        return S[r]
    else:
        return randSelect(greater, (k - (num_equal + num_less)))

