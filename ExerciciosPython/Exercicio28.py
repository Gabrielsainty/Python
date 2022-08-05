#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

aleatorio = random.randint(0,5)
print (aleatorio)
escolha = int(input('Qual número voce acha que a máquina escolheu? '))
if escolha == aleatorio:
    print('Monstruoso, voce acertou!')
else:
    print('Infelizmente voce errou, mais sorte na proxima vez...')