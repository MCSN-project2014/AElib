__author__ = 'dido-ubuntu'



############################################################################################################
####################################### TRIE data structure     ################################
############################################################################################################


class TrieArray():
    """
    Represent a Trie.
    Each node is implemented as a sigma-sized array [the alphabet size]
    Strings are stored in the leaves of the trie so we have n leaves as strings inserted..
    """

    def __init__(self, sigma, dictnaming):
        self.sigma = sigma  # alphabet is eqaul to the number of different key in the dictionary
        self.root = TrieNodeArray(self.sigma)
        self.dict_naming = dictnaming

    def insert(self, string):
        tempNode = self.root
        msdigit = 0
        self._insertRic(tempNode, string, msdigit)

    def _insertRic(self, node, string, msdigit):
        iDigitStr = self.dict_naming[string[msdigit]]  #n-th most significant digit associated to the char
        item = node.array[iDigitStr]
        if item is None :
            # insert the string because there is no other string
            node.array[iDigitStr] = string
        elif isinstance(item, str):
            # collision
            oldString = item
            newNode = TrieNodeArray(self.sigma)
            node.array[iDigitStr] = newNode
            msdigit += 1
            self._updateLevel(newNode, string, msdigit, oldString)
        elif isinstance(item, TrieNodeArray):
            msdigit = msdigit + 1
            self._insertRic(item, string, msdigit)

    def _updateLevel(self, node, newString, msdigit, oldString):
        """
        Insert the strings on a level node with the position
        """
        self._insertRic(node, newString, msdigit)
        self._insertRic(node, oldString, msdigit)


    def visitInOrder(self):
        if self.root == [None for i in range(self.sigma)]:
            return []
        def recVisit(node, list):
            for item in node.array:
                if isinstance(item, str):
                    list.append(item)
                elif isinstance(item, TrieNodeArray):
                    recVisit(item, list)
                elif item is None:
                    pass
            return list
        return recVisit(self.root, [])

    """
    # A recursive generetor that generates Tree leaves in in-order

    def inorder(self,t):
        if t:
            for x inorder(t.left):
                yield x
            yield t.label
            for x in inorder(t.right):
                yield x
    """

    def __str__(self):
        if self.root == [None for i in range(self.sigma)]:
            return '<empty TRIE>'
        def recurse(node, strNode):
            for item in node.array:
                if isinstance(item, str):
                    strNode = strNode + " " + item
                elif isinstance(item, TrieNodeArray):
                    strNode += recurse(item, strNode)
                elif item is None:
                    pass
            return strNode
        return recurse(self.root, " ")

class TrieNodeArray():
    """
    Represent a single Node in the trie.
    Each has a sigma-sized array.
    The leaves store the strings.
    """

    def __init__(self, sigma):
        self.sigma = sigma
        self.array = [None for i in range(self.sigma)]  # array[i] = [None] or Pointer to another TrieNode or String
        self.parent = None



###################################################
######################### Couting sort ###############
####################################################

def countingSort(array, k):
    """

    :param array: Array of n integer from integer [1,k]
    :param k: size of the alphabet.
    :return:
    """
    c = [0 for i in range(k)]       # c[i] = total number of integer  i in the array
    sorted = [None for i in range(len(array))]
    for j in range(0, len(array)):
        c[array[j]-1] += 1
    print(c)
    for i in range(1, k):
        c[i] += c[i-1]
    print(c)
    for j in range(len(array)-1, -1, -1):
        pos = c[array[j]-1]
        sorted[pos-1]= array[j]
        c[array[j]-1] -= 1
    return sorted
