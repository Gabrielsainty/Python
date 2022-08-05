#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.

numero = input('Digite um número de 0 a 9999: ')
print (f'O número que voce escolheu é {numero}')
print (f'A unidade é {numero[3]}, a dezena é {numero[2]}, a centena é {numero[1]} e o milhar é {numero[0]}')