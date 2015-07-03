
import heapq



def mergesort(list):
    """
     Merge sort implementation
    :param list:  list to be sorted
    :return: the list sorted
    """

    if len(list) <= 1:
        return list
    middle = len(list)//2
    left = list[:middle]
    right = list[middle:]
    left = mergesort(left)
    right = mergesort(right)
    res = merge(left, right)
    return res


def merge(left, right):
    """
    Merging left and right array in order
    :param left: left list of ordered elements
    :param right: rigth list of ordered elements
    :return: a list ordered
    """

    res = []
    while len(left) + len(right):
        if len(left) * len(right):
            if left[0] <= right[0]:
                res.append(left[0])
                left = left[1:]
            else:
                res.append(right[0])
                right = right[1:]
        elif len(left):
            res.append(left[0])
            left = left[1:]
        elif len(right):
            res.append(right[0])
            right = right[1:]
    return res

class SnowPlow():
    """
    Snow plow technique.
    """

    def __init__(self, s=[], sizeM=2):
        self.sizeM = sizeM
        self.s = s

    def createRuns(self):
        u = []
        for i in range(self.sizeM):
            u.append(self.s.pop(0))
        outRuns = []
        self._snowPlowPhase(u, outRuns)
        return outRuns

    def _snowPlowPhase(self, u, outRuns):
        run = []
        h = list(u)             # copy the item of u in h
        heapq.heapify(h)        # h as min-heap

        u = []
        while len(h) > 0:
            min = heapq.heappop(h)
            run.append(min)
            if len(self.s) > 0:
                next = self.s.pop(0)         # next element in the sequence
                if next < min:
                    u.append(next)
                else:
                    heapq.heappush(h, next)
        outRuns.append(run)
        if len(u) < self.sizeM:
            self._snowPlowPhase(u, outRuns)
        elif len(u) == self.sizeM:
            return outRuns

    def _merge(self, a, b):
        """
        a, b: vectors of orderd elements
        """
        aux = []
        x = 0
        y = 0
        tot = len(a)+len(b)
        for k in range(tot):
                if a[x] > b[y]:
                    aux.append(b[y])
                    y += 1
                elif a[x] < b[y]:
                    aux.append(a[x])
                    x += 1
                if y > k:  # prints y is at the end of the sequence
                    aux.append(a[x])
                    x += 1
        return aux

