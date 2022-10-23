#Desenvolva um programa que leia o primeiro termo e a razao de uma progressao aritmetica.No final, mostre os 10 primeiros termos dessa progressao.

c = int(input('Digite o valor inicial: '))
#f = int(input('Digite o valor final: '))
r = int(input('Digite a razão: '))
print (f'A PA começara em {c} e acabará em 10, com razão de {r}')

for a in range (c,10+1,r):
    print (a)

falta definir como colocar sempre 10 resultados.