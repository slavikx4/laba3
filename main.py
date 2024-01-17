import re

def display_letters(input_string):    letters_only = re.findall(r'[a-zA-Z]', input_string)
    result = ''.join(letters_only)    return result
