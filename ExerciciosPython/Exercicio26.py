#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "a"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece pela ultima vez

frase = input("Digite uma frase: ")
letra = input("Digite qual letra deseja procurar: ")
print ('A Letra "a" aparece na frase {} vezes.'.format(frase.count(letra)))
print ('A letra "a" aparece pela 1ª vez no index {}.'.format(frase.find(letra)))
print ('A letra "a" aparece pela ultima vez no index {}.'.format(frase.rfind(letra)))