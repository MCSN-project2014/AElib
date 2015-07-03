__author__ = 'dido-ubuntu'


class Cuckoo ():

    def __init__(self, m,  h1=lambda x: x, h2=lambda x: x):
        self.m = m
        self.h1 = h1
        self.h2 = h2
        self.table = [None for i in range(m)]

    def insert(self, key):
        if self.table[self.h1(key)] is None:
            print(self.table[self.h1(key)])
            print(self.h1(key))
            self.table[self.h1(key)] = key
        elif self.table[self.h2(key)] is None:
            print("key h2 : of"+str(key))
            print(self.h1(key))
            self.table[self.h2(key)] = key
        else:
            #both entries occupies by other keys
            evict1 = self.table[self.h1(key)]
            self.table[self.h1(key)] = key
            loop1 = self._insertEvict(evict1, key)
            if(loop1):
                evict2 = self.table[self.h2(key)]
                loop2 = self._insertEvict(evict2, key)
                if loop2 :
                    print("loop infinito")



    def _insertEvict(self, key, firstKey ):

        if key == firstKey :
            loop = True
            return loop
        if self.table[self.h1(key)] is None:
            self.table[self.h1(key)] = key
            return False
        elif self.table[self.h2(key)] is None:
            self.table[self.h2(key)] = key
            return False
        else:
            evicted = self.table[self.h1(key)]
            self.table[self.h1(key)] = key
            return self._insertEvict(evicted, firstKey)


c = Cuckoo(7,lambda x : x % 4, lambda y : (y*2) % 7)
s = [1,5,8,3,12,10,11,13,9]
c.insert(1)
c.insert(5)
c.insert(8)
c.insert(3)
c.insert(12)
c.insert(10)

print(c.table)
