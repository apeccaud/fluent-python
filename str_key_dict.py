class StrKeyDict(dict):
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

    def get(self, key, default=None):
        '''
        >>> d = StrKeyDict([('2', 'two'), ('4', 'four')])
        >>> d.get(2)
        'two'
        >>> d.get('4')
        'four'
        >>> d.get('5', 'def')
        'def'
        '''
        try:
            return self[key]
        except KeyError:
            return default

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
        return key in self.keys() or str(key) in self.keys()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
