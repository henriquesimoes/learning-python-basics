# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:17:32 2018

@author: Henrique Simões

Task: print the greatest number inserted by the user.
"""

number1 = float(input("Insira o primeiro número: "))
number2 = float(input("Insira o segundo número: "))

if number1 == number2:
    print("Os números inseridos são iguais")
else:
    if number1 > number2:
        result = number1
    else:
        result = number2
    print(result, "é o maior número inserido.")