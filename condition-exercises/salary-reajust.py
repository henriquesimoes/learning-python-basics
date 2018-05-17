# -*- coding: utf-8 -*-
"""
Created on Thu May 17 16:05:43 2018

@author: Henrique Simões
"""

salary = float(input("Entre com o salário: "))

if salary >= 0:
    if salary <= 280:
        tx = .2
    elif salary < 700:
        tx = .15
    elif salary < 1500:
        tx = .1
    else:
        tx = .05
        
print("Salario antes do reajuste:", salary)
print("Percentual de aumento aplicado:", tx * 100, "%")
print("Valor do aumento:", salary * tx)
print("Novo salário:", salary * (1 + tx))