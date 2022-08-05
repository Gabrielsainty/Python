#Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triangulo.

reta1 = float(input('Digite o valor da 1ª reta: '))
reta2 = float(input('Digite o valor da 2ª reta: '))
reta3 = float(input('Digite o valor da 3ª reta: '))

#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print ('O triangulo é possível com esses valores!.')
else:
    print ('O triângulo ficará irregular, então é impossivel com esses valores...')

if reta1 != reta2 or reta3:
    print('Esse triângulo é escaleno')