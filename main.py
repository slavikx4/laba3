import re

def display_letters(input_string):    letters_only = re.findall(r'[a-zA-Z]', input_string)
    result = ''.join(letters_only)    return result
if name == "__main__":
    user_input = input("Введите строку: ")    result_string = display_letters(user_input)
     if result_string:
        print("Буквы в введенной строке:", result_string)    else:
        print("В введенной строке нет букв.")
