#Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triangulo.

reta1 = float(input('Digite o valor da 1ª reta: '))
reta2 = float(input('Digite o valor da 2ª reta: '))
reta3 = float(input('Digite o valor da 3ª reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print ('O triangulo é possível com esses valores!.')
    if reta1 == reta2 == reta3:
        print('Esse triangulo é equilatero')
    elif reta1 == reta2 or reta1 == reta3 or reta3 == reta2:
        print('Esse triangulo é Isosceles')
    else:
        print('Esse triangulo é escaleno')
else:
    print ('O triângulo ficará irregular, então é impossivel com esses valores...')