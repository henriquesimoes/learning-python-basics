# -*- coding: utf-8 -*-
"""
Created on Thu May 10 13:51:06 2018

@author: Henrique Simões

Task: greet according to the time one studies
"""

print("Qual turno você estuda?\nM (Matutino)\nV (Vespertino)\nN (Noturno)")
shift = input("Opção: ")
if shift == "M":
    print("Bom dia!")
elif shift == "V":
    print("Boa tarde!")
elif shift == "N":
    print("Boa noite!")
else:
    print("Valor inválido")