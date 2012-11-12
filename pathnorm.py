# Using python version 3.3

from re import compile, match

UNIX = 0
DOS = 1
SEPARATORS = {UNIX: '/', DOS: '\\'}
DOS_PREFIX_PATTERN = compile('.*:')

def _isabs(path, system=UNIX):
    '''Determines whether the given pathname is an absolute path on the given
    system.

    If the given pathname is a relative path, this only returns False.
    Otherwise, it returns a tuple: one with the absolute path prefix, and one
    with the rest of the path.
    '''
    separator = SEPARATORS[system]
    if system == UNIX:
        if path[0] == separator:
            return (separator, path[1:])
    elif system == DOS:
        prefix = path.split(separator)[0]
        if DOS_PREFIX_PATTERN.match(prefix):
            return (prefix + separator, path[len(prefix) + 1:])
    return False

def _build_path_list(path, separator='/'):
    '''Returns a list containing the structure of directories represented by
    a relative path.'''
    
    contents = path.split(separator)
    structure = []
    
    for directory in contents:
        if directory == '.':
            pass
        elif directory == '..':
            if len(structure) == 0: # non-existent parent
                pass 
            else:
                structure.pop()
        else:
            structure.append(directory)

    return structure

def normalize(path, system=UNIX):
    '''Returns a normalized filepath string.'''
    if len(path) == 0:
        return path
    
    absolute = _isabs(path, system)
    if absolute:
        prefix, path = absolute
    else:
        prefix = ''
    
    separator = SEPARATORS[system]
    dirs = _build_path_list(path, separator) # holds directories on the path
    if dirs == None:
        return path
    else:
        return prefix + str.join(separator, dirs)

def _test():
    '''Run a test suite for this module.'''
    assert normalize('foo/bar') == 'foo/bar'
    assert normalize('/foo/bar') == '/foo/bar'
    assert normalize('/foo/./bar') == '/foo/bar'
    assert normalize('foo/./bar') == 'foo/bar'
    assert normalize('/foo/../bar') == '/bar'
    assert normalize('foo/../bar') == 'bar'
    assert normalize('/foo/bar/..') == '/foo'
    assert normalize('/foo/bar/../baz') == '/foo/baz'
    assert normalize('/foo/bar/../../baz/.') == '/baz'
    assert normalize('foo/..') == ''
    assert normalize('/foo/..') == '/'
    assert normalize('/foo//bar') == '/foo//bar'
    assert normalize('/') == '/'
    assert normalize('.') == ''
    assert normalize('..') == ''
    assert normalize('') == ''

    print('All tests have passed.')

if __name__ == '__main__':
    _test()
    path = input()
    while path != '':
        print(normalize(path, UNIX))
        path = input()
