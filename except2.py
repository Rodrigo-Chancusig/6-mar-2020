# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:28:15 2020

@author: CEC
"""

def reciproco(n):
    try:
        n=1/n
    except ZeroDivisionError:
        print("Division fallida")
        n=None
    else:
        print("Todo salio bien")
    finally:
        print("Es el momento de decir adios")
        return n

print(reciproco(2))
print(reciproco(0))