# -*- coding: utf-8 -*-
"""
Created on Thu May 10 13:39:49 2018

@author: Henrique Simões

Task: determinate which product is cheaper.
"""

prod1 = float(input("Preço do primeiro produto: "))
prod2 = float(input("Preço do segundo produto: "))
prod3 = float(input("Preço do terceiro produto: "))

if prod1<prod2 and prod1<prod3:
    print("Deve-se escolher o primeiro produto.")
elif prod2<prod1 and prod2<prod3:
    print("Deve-se escolher o segundo produto.")
elif prod3<prod1 and prod3<prod2:
    print("Deve-se escolher o terceiro produto.")
elif prod1==prod2 and prod1 < prod3:
    print("Deve-se escolher o primeiro ou o segundo produto.")
elif prod2==prod3 and prod2 < prod1:
    print("Deve-se escolher o segundo ou o terceiro produto.")
elif prod1==prod3 and prod1 < prod2:
    print("Deve-se escolher o primeiro ou o terceiro produto.")
else:
    print("Qualquer produto pode ser escolhido.")