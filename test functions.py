# Needs to be tweaked, second word not capitalizing.

def capitalized(two_words):
    '''(str) -> str

    Precondition: two_words is a string containing two words separated by one space.

    Return a string containing the words in two_words, but capitalized, again
    separated by one space.

    >>> capitalized('hello world')
    Hello World
    '''

    first = two_words[:two_words.find(' ')]
    second = two_words[two_words.find(' '):]
    return first.capitalize() + ' ' + second.capitalize()


def count_max_letters(s1, s2, letter):
    '''(str, str, str) -> int

    s1 and s2 are strings, and letter is a string of length 1.  Count how many
    times letter appears in s1 and in s2, and return the bigger of the two
    counts.

    >>> count_max_letters('hello', 'world', 'l')
    2
    >>> count_max_letters('cat', 'abracadabra', 'a')
    5
    '''

    return max(s1.count(letter), s2.count(letter))

# Add an example

def same_length(L1, L2):
    '''(list, list) -> bool

    Return True if and only if L1 and L2 contain the same number of elements.
    '''
    return len(L1) == len(L2)


def reverse(s):
    '''(str) -> str

    Return the reverse of s.

    >>> reverse('abc')
    'cba'
    >>> reverse('a')
    'a'
    >>> reverse('madam')
    'madam'
    >>> reverse('1234!')
    '!4321'
    '''

    result = ''
    i = len(s) - 1
    while i >= 0:
        result = result + s[i]
        i = i - 1

    return result

def get_keys(L, d):
    '''(list, dict) -> list

    Return a new list containing all the items in L that are keys in d.

    >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
    [1, 'a']
    '''

    result = []
    for k in L:
        if k in d:
            result.append(k)

    return result



# Not finished

def double_values(collection):
    for v in range(len(collection)):
        collection[v] = collection[v] * 2


def get_negative_nonnegative_lists(L):
    '''(list of list of int) -> tuple of (list of int, list of int)

    Return a tuple where the first item is a list of the negative ints in the
    inner lists of L and the second item is a list of the non-negative ints
    in those inner lists.

    Precondition: the number of rows in L is the same as the number of
    columns.

    >>> get_negative_nonnegative_lists([[-1,  3,  5], [2,  -4,  5], [4,  0,  8]])
    ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
    '''

    nonneg = []
    neg = []
    for row in range(len(L)):
        for col in range(len(L)):
              if L[row][col] < 0:
                neg.append(L[row][col])
              elif L[row][col] >= 0:
                nonneg.append(L[row][col])
    return (neg, nonneg)


# Not finished

def are_lengths_of_strs(L1, L2):
    '''(list of int, list of str) -> bool

    Return True if and only if all the ints in L1 are the lengths of the strings
    in L2 at the corresponding positions.

    Precondition: len(L1) == len(L2)

    >>> are_lengths_of_strs([4, 0, 2], ['abcd', '', 'ef'])
    True
    '''

    result = True
    for i in range(len(L1)):
        if i != len(L2[0:-1]):
            result = False

    return result

# Not finished

def count_chars(s):
    '''(str) -> dict of {str: int}

    Return a dictionary where the keys are the characters in s and the values
    are how many times those characters appear in s.

    >>> count_chars('abracadabra')
    {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
    '''
    d = {}

    for c in s:
        if not (c in d):
            d[c] = c
        else:
            d[c] = d[c] + 1

    return d
