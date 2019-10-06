#!/usr/bin/python3
"""
text identation module:
indents text
useful
"""


def text_indentation(text):
    """text must be a string, There should be no space
    at the beginning
    or at the end of each printed line.
    """
    # text is a string, otherwise raise a TypeError
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    # if text is None or not isinstance(text, str) or len(text) < 0:
    # raise TypeError('must be a string')
    # string.replace(old, new, count)
    # prints a text with 2 new lines
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    # 1) cut the entire line with \n
    # 2) cut by separator with \n
    # to the line that was strip (for.,?)
    # loop text and split where "\n" is)
    # end =""no space output promp line)
    # there should be no spaces at the beginning
    # and the end, line strip metodo

    print("\n".join([line.strip() for line in text.split("\n")]), end="")

    # if isinstance(text, str) is False:
    # raise TypeError("text must be a string")
    # delim = ":.?"
    # for x in delim:
    # text = text.replace(x, "{}\n\n".format(x))
    # text = text.replace('\\', '')
    # text = "\n".join([line.strip() for line in text.split('\n')])
    # print(text, end="")
