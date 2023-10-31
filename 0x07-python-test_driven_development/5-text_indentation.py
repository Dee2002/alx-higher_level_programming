#!/usr/bin/python3
'''
Function that prints 2 new lines after each of these characters: ., ? and :
Usage:
text_indentation(text)
'''


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    result = ""
    for char in text:
        result += char
        if char in special_chars:
            result += "\n\n"

    print(result)
