


__author__ = 'dido-ubuntu'

############################################################################################################
####################################### TRIE data structure     ################################
############################################################################################################


class Trie():
    """
    Represent a compacted Trie.
    Each node is implemented as a sigma-sized array [the alphabet size]

    Strings are stored in the leaves of the trie so we have n leaves as strings inserted..
    """

    def __init__(self, sigma, dictnaming):
        self.sigma = sigma  # alphabet is eqaul to the number of different key in the dictionary
        self.root = TrieNode(self.sigma)
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
            newNode = TrieNode(self.sigma)
            node.array[iDigitStr] = newNode
            msdigit += 1
            self._updateLevel(newNode, string, msdigit, oldString)
        elif isinstance(item, TrieNode):
            msdigit = msdigit + 1
            self._insertRic(item, string, msdigit)

    def _updateLevel(self, node, newString, msdigit, oldString):
        """
        Insert the strings on a level node with the position
        """
        self._insertRic(node, newString, msdigit)
        self._insertRic(node, oldString, msdigit)

    """
    def __str__(self):
        if self.root == [None for i in xrange(self.sigma)]:return '<empty tree>'
        def recurse(node):
            if node == [None for i in xrange(self.sigma)]: return [], 0, 0
            label = "nodo" #str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])

    """
    def visitInOrder(self):
        if self.root == [None for i in range(self.sigma)]:
            return []
        def recVisit(node, list):
            for item in node.array:
                if isinstance(item, str):
                    list.append(item)
                elif isinstance(item, TrieNode):
                    recVisit(item, list)
                elif item is None:
                    pass
            return list
        return recVisit(self.root, [])

    def __str__(self):
        if self.root == [None for i in range(self.sigma)]:
            return '<empty TRIE>'
        def recurse(node, strNode):
            for item in node.array:
                if isinstance(item, str):
                    strNode = strNode + " " + item
                elif isinstance(item, TrieNode):
                    strNode += recurse(item, strNode)
                elif item is None:
                    pass
            return strNode
        return recurse(self.root, " ")

class TrieNode():
    """
    Represent a single Node in the trie.
    Each has a sigma-sized array.
    The leaves store the strings.
    """

    def __init__(self, sigma):
        self.sigma = sigma
        self.array = [None for i in range(self.sigma)] # array[i] = [None] or Pointer to another TrieNode or String
        self.parent = None

############################################################################################################
####################################### BINARY SEARCH TREEE  DATA STRUCTURE ################################
############################################################################################################


class BST( ):
    """
    Simple binary search tree implementation.
    This BST supports insert, find, and delete-min operations.
    Each tree contains some (possibly 0) BSTnode objects, representing nodes,
    and a pointer to the root.
    """

    def __init__(self):
        self.root = None

    def insert(self, t):
        """Insert key t into this BST, modifying it in-place."""
        new = BSTnode(t)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                if t < node.key:

                    if node.left is None:
                        node.left = new
                        new.parent = node
                        break
                    node = node.left
                else:
                    # Go right
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return new

    def find(self, t):
        """Return the node for key t if is in the tree, or None otherwise."""
        node = self.root
        while node is not None:
            if t == node.key:
                return node
            elif t < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def delete_min(self):
        """Delete the minimum key (and return the old node containing it)."""
        if self.root is None:
            return None, None
        else:
            # Walk to leftmost node.
            node = self.root
            while node.left is not None:
                node = node.left
            # Remove that node and promote its right subtree.
            if node.parent is not None:
                node.parent.left = node.right
            else: # The root was smallest.
                self.root = node.right
            if node.right is not None:
                node.right.parent = node.parent
            parent = node.parent
            node.disconnect()
            return node, parent


    def inOrderVisit(self):
        """
        In order visit of the tree
        """
        node = self.root
        itmVisited = []
        return self._inOrder(node, itmVisited)

    def _inOrder(self, node, itemsVisited):

        if(node is not None):
            listleft = self._inOrder(node.left, itemsVisited)
            listleft = listleft + [node.key]
            listRigth = self._inOrder(node.right, itemsVisited)
            itemsVisited = listleft + listRigth
        return itemsVisited





    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])

class BSTnode(object):
    """
    Representation of a node in a binary search tree.
    Has a left child, right child, and key value.
    """
    def __init__(self, t):
        """Create a new leaf with key t."""
        self.key = t
        self.disconnect()

    def disconnect(self):
        self.left = None
        self.right = None
        self.parent = None


def test(args=None, BSTtype=BST):
    import random, sys
    if not args:
        args = sys.argv[1:]
    if not args:
        print( 'usage: %s <number-of-random-items | item item item ...>' % sys.argv[0])
        sys.exit()
    elif len(args) == 1:
        items = (random.randrange(100) for i in range(int(args[0])))
    else:
        items = [int(i) for i in args]

    tree = BSTtype()
    print (tree)
    for item in items:
        tree.insert(item)

    print(tree)
    print(tree.inOrderVisit())


