# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 13:43:05 2018

@author: Henrique Simões
"""

degree = int(input("Entre com uma temperatura: "))

print(degree, "°F é igual a ", (5 * (degree - 32))/9, "°C")
print(degree, "°C é igual a ", 9 * degree / 5 + 32, "°F")