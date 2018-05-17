# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:16:26 2018

@author: Henrique Simões
"""

score1 = float(input("Entre com a primeira nota (0-10): "))
score2 = float(input("Entre com a segunda nota (0-10): "))

print("As notas inseridas foram:", score1, "e", score2)

if score1<0 or score1>10 or score2<0 or score2>10:
    print("Notas inválidas")
else:
    avarage = (score1 + score2) / 2
    print("Média semestral:", avarage)
    if avarage < 4:
        concept = "E"
    elif avarage < 6:
        concept = "D"
    elif avarage < 7.5:
        concept = "C"
    elif avarage < 9:
        concept = "B"
    else:
        concept = "A"
    print("Conceito:", concept)
    if concept == "A" or concept == "B" or concept == "C":
        result = "APROVADO"
    elif concept == "E" or concept == "D":
        result = "REPROVADO"
    print("O aluno foi", result)