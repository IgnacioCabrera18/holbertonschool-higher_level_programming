#!/usr/bin/python3
def islower(c):
    for i in c:        
        if i == "":
            return
        elif i.islower():
            return True
        else:
            return False
