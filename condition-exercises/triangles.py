# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:36:20 2018

@author: Henrique Simões
"""
sides = [0,0,0]
sides[0] = float(input("Entre com a dimensão do primeiro lado: "))
sides[1] = float(input("Entre com a dimensão do segundo lado: "))
sides[2] = float(input("Entre com a dimensão do terceiro lado: "))

if not((sides[0] + sides[1] > sides[2]) and
   (sides[0] + sides[2] > sides[1]) and
   (sides[1] + sides[2] > sides[0])):
    print("Não forma um triângulo")
else:
    if(sides[0] == sides[1] and sides[1] == sides[2]):
        triangle_type = "equilátero"
    elif(sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]):
        triangle_type = "escaleno"
    else:
        triangle_type = "isósceles"
    print("Pode formar um triagulo", triangle_type)