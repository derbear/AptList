# Using python version 3.3

SEPARATOR = '/' # for Unix systems

def _build_path_list(path, separator='/'):
    '''Returns a list containing the structure of directories represented by
    the path.'''
    
    contents = path.split(separator)
    structure = []
    
    for directory in contents:
        if directory == '.':
            pass
        elif directory == '..':
            if len(structure) == 0: # non-existent parent
                pass # unsure what to do, failure case?
            else:
                structure.pop()
        else:
            structure.append(directory)

    return structure

def normalize(path, separator='/'):
    '''Returns a normalized filepath string.'''
    dirs = _build_path_list(path, separator) # holds directories on the path
    if dirs == None:
        return path
    else:
        return str.join(separator, dirs)

def _test():
    '''A function containing a test suite for this module.'''
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
    assert normalize('/') == '/'
    assert normalize('.') == ''
    assert normalize('/foo//bar') == '/foo//bar'
    print('All tests have passed.')

if __name__ == '__main__':
#    _test()
    path = input()
    while path != '':
        print(normalize(path, SEPARATOR))
        path = input()
