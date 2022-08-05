#Escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento:
#Para salarios superiores a R$ 1250, calcule um aumento de 10%, e para inferiores ou iguais, calcule de 15%

din = int(input('Digite seu salário: '))
if din <= 1250:
    aum = din * 15 / 100
    print (f'Esse salário está dentro da lista de aumentos de 15%, se tornando portanto R${din + aum:.2f}.')
else:
    aum = din * 10 / 100
    print (f'Esse salário está dentro da lista de aumentos de 10%, se tornando portanto R${din + aum:.2f}.')