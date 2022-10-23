#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços

pld = 'LOUCO COMO UM GATO' [::-1]
pld[::-1] == pld
print (pld.strip())
pld.strip()