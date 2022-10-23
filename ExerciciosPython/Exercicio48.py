#Faça um programa que calcule a soma de todos os numeros impares que sao multiplos de 3 e que se encontram no intervalo entre 1 e 500.

for c in range(3,500+1):
    if c%3==0 and c%2==1:
        print (c)