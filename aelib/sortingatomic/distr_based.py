
import heapq
import random



def quicksort(seq, i, j):
    """
    l = index[0]
    r = index[1]
    s[l,...r] == pivot selected
    """
    if i < j:
        r = random.randint(i, j)  # pivot position selection
        swap(seq, r, i)
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
            swap(seq, c, r)
            r += 1
        elif seq[c] < P:
            swap(seq, c, l)
            swap(seq, c, r)
            l += 1
            r += 1
    ret = [l, r-1]
    return ret


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return array

"""
def RandSelect( S , k ):
    RandomizeD algorithm that select the item of the unordered S having rank k

    r = S[random.randint( 0, len(S)-1 ) # select a random element
"""

def