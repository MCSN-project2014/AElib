
import heapq
import random



def QuickSort( S , i , j ):
    """
    l = index[0]
    r = index[1]
    s[l,...r] == pivot selected
    """
    if( i < j):
        r = random.randint( i, j )  # pivot position selection
        swap( S , r , i )
        index = _threePartition( S, i,j )
        QuickSort( S , i , index[0]-1 )
        QuickSort( S , index[1]+1 , j  )


def _partition( S , i , j):
    """
    The pivot selected is in the S[i] position
    Divid s S in two sub arrays
    S[i,...,p-1] < S[p]
    S[p+1, ...,n] > S[p]
    """

def _threePartition( S , i , j):
    """
    S[i] contains the pivot.
    If the sequence scanned id S[ i , c-1]:
    S[ i , ... , l-1 ] < P
    S[ l , ... , r-1 ] = P
    S[ r , ... , c-1 ] > P

    Return vector I of the central sub-array containig all the equal items
    """
    ret = []
    P = S[i]
    l = i
    r = i+1
    for c in range( r, j+1 ):
        if( S[c] == P):
            swap( S, c, r )
            r += 1
        elif( S[c] < P):
            swap( S, c, l )
            swap( S, c, r )
            l += 1
            r += 1
    ret = [l,r-1]
    return ret

def swap( S, i, j ):
    temp = S[i]
    S[i] = S[j]
    S[j] = temp
    return S

"""
def RandSelect( S , k ):
    RandomizeD algorithm that select the item of the unordered S having rank k

    r = S[random.randint( 0, len(S)-1 ) # select a random element
"""
