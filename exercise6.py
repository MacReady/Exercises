
def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the right
    and shift the last item to the first position.

    Precondition: len(L) >= 1

    >>> shift_right(['a', 'b', 'c', 'd'])
    ['d', 'a', 'b', 'c']
    '''

    last_item = L[-1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]

    L[0] = last_item

    return L

def shift_left(L):
    ''' (list) -> NoneType
    
    Shift each item in L one position to the left and shift the first item to
    the last position.
    
    Precondition: len(L) >= 1
    
    >>> shift_left(['a', 'b', 'c', 'd'])
    ['b', 'c', 'd', 'a']
    '''
    
    first_item = L[0]
    
    for i in range(len(L) - 1):
        L[i] = L[i + 1]
    
    L[-1] = first_item

    return L

# List is repeating three times, needs to be fixed

def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list
    
    Return a new list in which each item is a 2-item list with the string from the
    corresponding position of list1 and the int from the corresponding position of list2.
    
    Precondition: len(list1) == len(list2)
    
    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]] 
    '''
    
    pairs = []
    
    inner_list = []
    for i in range(len(list1)):
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)
        
    return pairs




def contains(value, lst):
    ''' (object, list of list) -> bool

    Return whether value is an element of one of the nested lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]])
    True
    '''

    found = False

    for sublist in lst:
        if value in sublist:
            found = True

    return found    



def lines_startswith(file, letter):
    '''(file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter. The lines should have the
    newline removed.

    Precondition: len(letter) == 1
    '''

    matches = []

    for line in file:
        if letter == line[0]:
            matches.append(line.rstrip('\n'))
        
    return matches


def write_to_file(file, sentences):
    '''(file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    '''

    for s in sentences:
        file.write(s)
