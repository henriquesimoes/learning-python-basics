# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:43:35 2018

@author: Henrique Simões

Task: print the greatest number inserted by the user.
"""

number1 = float(input("Insira o primeiro número: "))
number2 = float(input("Insira o segundo número: "))
number3 = float(input("Insira o terceiro número: "))

if number1 > number2 and number1 > number3:
    result = number1;
elif number2 > number1 and number2 > number3:
    result = number2
else:
    result = number3
print(result, "é o maior número inserido.")