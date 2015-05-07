
import heapq





def mergesort(list):
    """
     Merge sort implementation
    :param list:  list to be sorted
    :return: the list sorted
    """

    if len(list)<=1:
        return list
    middle=len(list)/2
    left = list[:middle]
    right=list[middle:]
    left=mergesort(left)
    right=mergesort(right)
    res=merge(left,right)
    print (res)
    return res


def merge(left,right):
    """
     Merging left and right array in order
    :param left: left list of ordered elements
    :param right: rigth list of ordered elements
    :return: a list ordered
    """

    res=[]
    while len(left)+len(right):
        if len(left)*len(right):
            if left[0]<=right[0]:
                res.append(left[0])
                left=left[1:]
            else:
                res.append(right[0])
                right=right[1:]
        elif len(left):
            res.append(left[0])
            left=left[1:]
        elif len(right):
            res.append(right[0])
            right=right[1:]
    return res

class SnowPlow():

    def __init__(self,s=[],sizeM=2):
        self.sizeM = sizeM
        self.s = s
        u = []
        self.outRuns = []
        for i in range(self.sizeM):
            u.append(s.pop(0))
        self._snowPlowPhase(u)
        print (self._merge( self.outRuns[0],self.outRuns[1]))

    def _merge(self , a , b ):
        """
        a, b: vectors of orderd elements
        """
        aux =[]
        x = 0
        y = 0
        tot = len(a)+len(b)
        for k in range (tot):
                if(a[x] > b[y]):
                    aux.append(b[y])
                    y+=1
                elif(a[x] < b[y]):
                    aux.append(a[x])
                    x+=1
                if( y > k):  # pinter y is at the end of the sequence
                    aux.append(a[x])
                    x+=1
        return aux


    #@staticmethod
    def _snowPlowPhase(self, u):
        run =[]
        h = u
        heapq.heapify(h)           # u as min-heap
        u = [ ]
        while(len(h)>0):
            min = heapq.heappop(h)
            run.append(min)
            if(len(self.s)>0):
                next = self.s.pop(0)         # next element in the sequence
                if(next < min):
                    u.append(next)
                else:
                    heapq.heappush( h, next)
        self.outRuns.append(run)

        if(len(u)!=0):
            self._snowPlowPhase(u)



__author__ = 'dido-ubuntu'
