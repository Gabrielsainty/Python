#Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual será a base de conversão:
#1:Binario
#2:Octal
#3:Hexadecimal

num = int(input('Digite um numero inteiro:'))
bina = 1
octa = 2
hexa = 3
print ('''(1) para converter para Binário
(2) para converter para Octal
(3) para converter para Hexadecimal''')
escolha = int(input('Escolha para qual base de conversão você deseja converter: '))
if escolha == 1:
    print(f'A conversão de {num} para Binário é {bin(num)[2:]}.')
    #print(f'\033[1;35mA conversão de {num} para Binário é {bin(num)}.\033[m')
    #cbin = num
elif escolha == 2:
    print(f'\033[1;35mA conversão de {num} para Octal é {oct(num)[2:]}.\033[m')
    #coct = num
elif escolha == 3:
    print(f'\033[1;35mA conversão de {num} para Hexadecimal é {hex(num)[2:]}.\033[m')
    #chex = num
else:
    print('Você não escolheu uma opção válida, por favor escolha uma das opções')
    quit

#é necessário colocar o [2:] para filtrar o prefixo d ocodigo usado, em que o resultado aparece 2 caracteres iniciais.