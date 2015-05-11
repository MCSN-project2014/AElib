__author__ = 'dido-ubuntu'


def front_coding(dictStrings):
    """

    :param dictionary:
    :return:
    """
    fcoded = []
    for key, string in dictStrings.items():
        if len(fcoded) == 0:
            fcoded.append((0, string))
        else:
            prev_string = dictStrings[key-1]
            l = _compress(prev_string, string)

            if l > 0:
                fcoded.append((l, string[l:])) # tuple (<li>,<s'i>): li length of the longest coomon prefix with S(i-1), s'i: remain suffix
            else:
                fcoded.append((l, 0))
    return fcoded


def _compress(prev_string, string):

    l = 0
    for i in range(len(prev_string)):
        if i < len(string) and string[i] == prev_string[i]:
            l += 1
        else:
            break
    return l


