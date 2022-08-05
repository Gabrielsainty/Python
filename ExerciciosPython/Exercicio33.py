#Faça um programa que leia tres numeros e mostre qual o menor e qual o maior

add0 = [input('Digite um número: ')]
add1 = [input('Digite mais um número: ')]
add2 = [input('Digite um outro número: ')]
lista = add0 + add1 + add2
print (f'O menor valor que foi inserido foi {min(lista)}.')
print (f'O maior valor que foi inserido foi {max(lista)}.')
