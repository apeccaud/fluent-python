import collections


class StrKeyDict(collections.UserDict):
    '''
    Enhanced version of a standard dict supporting looking up values using
    either a string or int index
    '''

    def __missing__(self, key):
        '''
        >>> d = StrKeyDict([('2', 'two'), ('4', 'four')])
        >>> d['2']
        'two'
        >>> d[4]
        'four'
        >>> d[1]
        Traceback (most recent call last):
        ...
        KeyError
        '''
        if isinstance(key, str):
            raise KeyError
        return self[str(key)]

    def __contains__(self, key):
        '''
        >>> d = StrKeyDict([('2', 'two'), ('4', 'four')])
        >>> '2' in d
        True
        >>> 4 in d
        True
        >>> 5 in d
        False
        >>> '5' in d
        False
        '''
        return str(key) in self.data

    def __setitem__(self, key, item):
        '''
        >>> d = StrKeyDict()
        >>> d[1] = 'one'
        >>> d.keys()
        KeysView({'1': 'one'})
        '''
        self.data[str(key)] = item


if __name__ == '__main__':
    import doctest
    doctest.testmod()
