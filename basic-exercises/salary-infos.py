# -*- coding: utf-8 -*-
"""
Created on Tue May 1 16:35:07 2018

@author: Henrique Simões

"""

salary = float(input("Informe seu salário por hora: R$"))
hoursWorking = float(input("Informe a quantidade de horas trabalhadas no mês: "))
rawSalary = salary*hoursWorking
irTax = 0.11
inssTax = 0.08
sindTax = 0.05
print(" - Salário Bruto: R$", rawSalary)
print(" - IR (11%): R$", rawSalary*irTax)
print(" - INSS (8%): R$", rawSalary*inssTax)
print(" - Sindicato (5%): R$", rawSalary*sindTax)
print(" - Salário Líquido: R$", rawSalary*(1 - inssTax - irTax - sindTax))
