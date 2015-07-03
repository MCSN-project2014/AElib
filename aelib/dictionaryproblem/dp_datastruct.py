__author__ = 'dido-ubuntu'


class HashTable ():

    """
    Implement a sample Hash table with chaining,
        - t : is an array of lists
        - m : the number of keys

    """

    def __init__(self, m, hashfunction = lambda x: x):
        self.t = [[] for i in range(0, m)]
        self.hashfunction = hashfunction

    def insert(self, k):
        """
        Insert a new key in the table with the hash function
        """
        self.t[self.hashfunction(k)].append(k)


    def search(self, k):
        list = [x for x in self.t[self.hashfunction(k)] if x == k]
        return list if len(list) > 0 else None

    def delete(self, k):
        for chain in self.t:
            if k in chain:
                chain.remove(k)

    def __len__ (self):
        num_elements = 0
        for chain in self.t:
            num_elements += len(chain)
        return num_elements

    def __str__(self):
        string = "Hash table with chaining : \n"
        for chain in self.t:
            string += str(chain) +"\n"
        return string

"""
h = HashTable(3, lambda x : x % 3)
h.insert(5)
h.insert(2)
h.insert(2)
print(len(h))
h.delete(2)
print(len(h))
"""