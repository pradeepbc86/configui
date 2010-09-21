import string

valid_characters = string.join([string.letters, string.digits, '_'], '')
print valid_characters 
def coherse_name(name):
    '''
    Formats a string to be a valid filename, striping out everything
    except for letters, digits, and '_'
    '''
    _name = ''
    for character in name:
        if character in valid_characters:
            _name = string.join([_name,character],'')
    return _name
