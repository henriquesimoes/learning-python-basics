# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:55:34 2018

@author: Henrique Simões

Task: Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e 
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

import math
area = float(input("Entre com a área a ser pintada:"))
latas = math.ceil((area/3)/18)
preco = latas * 80
print("Serão necessárias", latas, "latas, que custarão, ao todo, R$", preco)