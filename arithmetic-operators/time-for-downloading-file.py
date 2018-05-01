# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:57:25 2018

@author: Henrique Simões

Task: Faça um programa que peça o tamanho de um arquivo para download (em MB) e 
a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

megabytes = float(input("Tamanho do arquivo (em MB): "))
speed = float(input("Velocidade de um link de Internet: "))
print("O tempo gasto será de aproximadamente", round((((megabytes/8)/speed)/60), 2), " minuto(s)")
