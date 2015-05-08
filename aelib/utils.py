from aelib.datastructure import datastruct


def naming(array_strings):
    """
    Naming process: assign to each characters in the strings
    an integer (rank) in the range {0,..., sigma-1}
    where sigma is the size of the alphabet.

    :rtype : Dictionary
    :param array_strings:  array of strings to be named
    :return: the dictionary with key a character and value the rank
    """

    tree = datastruct.BST()
    dict_naming = dict()
    for string in array_strings:
        for char in string:
            if tree.find(char) is None:
                tree.insert(char)

    ordered_char = tree.inOrderVisit() # list of ordered characters appears in the strings

    i = 0;
    for char in ordered_char:
        dict_naming[char] = i
        i += 1

    return dict_naming

__author__ = 'dido-ubuntu'