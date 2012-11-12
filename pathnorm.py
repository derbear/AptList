# Using python version 3.3

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

def normalize(path):
    '''Returns a normalized filepath string.'''
    if len(path) == 0:
        return path
    if path[0] == '/': # this path is absolute
        prefix = '/'
        path = path[1:]
    else: # this path is relative
        prefix = '' 
        
    dirs = _build_path_list(path, '/') # holds directories on the path
    if dirs == None:
        return path
    else:
        return prefix + str.join('/', dirs)

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
    # poll for input until EOF and apply normalize
    try:
        line = input()
        while True:
            paths = line.split(' ')
            for path in paths:
                print(normalize(path))
            line = input()
    except EOFError:
        pass
