import datastruct



def naming(arrayStrings):
    """

    :rtype : Dictionary
     Naming process: assign to each characters in the strings
    an integer(rank) in the range {0,..., sigm a-1}
    where sigma is the Alphabet originated from the strings passed as argument

    :param arrayStrings:  array of strings to be named
    :return: the dictionary with key a character and value the rank
    """

    tree = datastruct.BST()
    naming = dict()
    for s in arrayStrings:
        for char in s :
            if(tree.find(char) is None):
                tree.insert(char)

    orderCharacters = tree.inOrderVisit() # list of ordered characters appears in the strings

    i=0;
    for char in orderCharacters:
        naming[char]= i
        i=i+1

    return naming


__author__ = 'dido-ubuntu'