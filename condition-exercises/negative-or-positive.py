# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:34:24 2018

@author: Henrique Simões

Task: determine whether a number inserted by the user is negative or positive.
"""

number = float(input("Insira um valor: "))

if number >= 0:
    print(number, "is positive.")
else:
    print(number, "is negative.")