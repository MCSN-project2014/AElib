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

#####################################################
##################  TRIE with hash chaining #########
#####################################################


class TrieNodeHash():

    def __init__(self):
        pass


#####################################################
##################  Binary Search tree ##############
#####################################################

class BinarySearchTree():

    def __init__(self):
        self.root = None

    def insert(self, valueChild):
        if self.root is None:
            self.root = BinaryNode(valueChild)
            return  True
        else:
            self.root.insert(valueChild)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def inorderVisit(self):
        print("Inorder visit:")
        self.root.inorder()




class BinaryNode():

    def __init__(self, value, rigthChild=None, leftChild=None):
        self.value = value
        self.rigth_child = rigthChild
        self.left_child = leftChild


    def insert(self, data):
        if self.value == data:
            return False
        elif data < self.value:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = BinaryNode(data)
                return True
        else:
            if self.rigth_child:
                return self.rigth_child.insert(data)
            else:
                self.rigth_child = BinaryNode(data)
                return True

    def find(self, data):
        if self.value == data:
            return True
        elif data < self.value:
            if self.left_child:
                return self.left_child.find(data)
            else:
                return False
        else:
            if self.rigth_child:
                return self.rigth_child.find(data)
            else:
                return False

    def inorder(self):

        if self:
            if self.left_child:
                self.left_child.inorder()
            print(str(self.value))
            if self.rigth_child:
                self.rigth_child.inorder()

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
    for i in range(1, k):
        c[i] += c[i-1]
    for j in range(len(array)-1, -1, -1):
        pos = c[array[j]-1]
        sorted[pos-1]= array[j]
        c[array[j]-1] -= 1
    return sorted


b = BinarySearchTree()
b.insert(1)
b.insert(5)
b.insert(4)
b.insert(6)
print(b.find(6))
print(b.find(0))
b.inorderVisit()