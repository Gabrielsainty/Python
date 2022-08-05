#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porçao inteira. Ex: 6.127 tem a parte inteira 6.
from math import trunc

'''import math
print ('A parte inteira de {} é {}.'.format(num, math.trunc(num)))
#Caso eu quisesse fazer com o modulo completo de math nesse exemplo, eu deveria fazer ...format(num, math.trunc(num))) mas com import math antes do programa'''

num = float(input("Digite um numero: "))
print ('A parte inteira de {} é {}.'.format(num, trunc(num)))
