# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:30:30 2018

@author: Henrique Simões

Task: Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo 
    que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""

height = float(input("Altura em metros: "))
print("Peso ideal:", (72.7*height-58), "kg")