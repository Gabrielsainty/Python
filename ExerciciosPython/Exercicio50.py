#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))
num4 = int(input('Digite um numero: '))
num5 = int(input('Digite um numero: '))
num6 = int(input('Digite um numero: '))

soma = 0

if num1%2==0:
    soma += num1 
if num2%2==0:
    soma += num2
if num3%2==0:
    soma += num3
if num4%2==0:
    soma += num4
if num5%2==0:
    soma += num5
if num6%2==0:
    soma += num6

print (soma)

Agora aprender a fazer isso com loop...