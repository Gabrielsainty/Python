#Refaça o desafio 9 mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laço for.

#Exercicio 9:
#Faça um programa que leia um numero Inteiro qualquer e mostre na tela a sua tabuada

#i= int(input("Digite um número: "))
#i= int(input("\033[0;1mDigite um número: \033[0;1m"))
#print (f'A tabuada do {i} é {i*1},{i*2},{i*3},{i*4},{i*5},{i*6},{i*7},{i*8},{i*9},{i*10}')

#Exercicio 49:

i= int(input("Digite um número: "))
c= int(input("Digite até qual numero da tabuada: "))
print (f'A tabuada do {i} é:')
for c in range(1,c+1):
    print (f'{i}x{c}={i*c}.')