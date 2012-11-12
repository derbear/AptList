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

    # check whether path is relative or absolute
    if path[0] == '/': 
        prefix = '/'
        path = path[1:]
    else: 
        prefix = '' 
        
    dirs = _build_path_list(path, '/') 
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

def run():
    '''Polls standard input and writes normalized file paths to standard output
    until reaching EOF.'''
    try:
        line = input()
        while True:
            paths = line.split(' ')
            for path in paths:
                print(normalize(path))
            line = input()
    except EOFError:
        pass

if __name__ == '__main__':
    run()

