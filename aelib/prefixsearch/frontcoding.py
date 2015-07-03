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

def front_decoding(arrayTuples):
    """

    :param arrayTuples:  array of tuples coded with fron coding = [ (l,s),(l1;s'1)...]
    :return:  dictionary of decoded strings in alphabetic order { 0: "first", 1:"second"}
    """
    dictdecoded= {}
    prevstring = ""
    i = 0
    for l, codstr in arrayTuples:
        if l > 0:
            firststring = prevstring[:l]
            decodestring =  firststring + codstr
            dictdecoded[i] = decodestring
            prevstring = decodestring
            i += 1
        else:
            dictdecoded[i] = codstr
            prevstring = codstr
            i +=1
    return dictdecoded




def _compress(prev_string, string):

    l = 0
    for i in range(len(prev_string)):
        if i < len(string) and string[i] == prev_string[i]:
            l += 1
        else:
            break
    return l


