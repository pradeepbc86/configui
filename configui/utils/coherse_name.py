import string

valid_characters = string.join([string.letters, string.digits, '_'], '')
def coherse_name(name):
    '''
    Formats a string to be a valid filename, striping out everything
    except for letters, digits, and '_'
    '''
    cohersed_name = ''
    space_replaced_name = name.replace(' ', '_')
    for character in space_replaced_name:
        if character in valid_characters:
            cohersed_name = string.join([cohersed_name,character],'')
    return cohersed_name
