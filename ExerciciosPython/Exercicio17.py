#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo , calcule e mostre o comprimento da hipotenusa.
import math

catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimento do cateto adjacente: '))

#hip = (catop**2 + catad**2) ** 1/2 Essa é a versão matematica pura dessa conta, as duas fazem a mesma operação
hip = math.hypot(catop, catad)
print (f'O valor da hipotenusa é {hip:.3f}!')