#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    temp = ""
    for char in text:
        temp += char
        if char in ".:?":
            print(temp.strip(), end="\n\n")
            temp = ""
    if temp.strip():
        print(temp.strip(), end="")
