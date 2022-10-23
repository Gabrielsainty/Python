#Faça um programa que mostre uma contagem regressiva para estouro de fogos de artificio, indo de 10 ate 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print ('O Ano novo vai acontecer em: ')
for c in range (10, 0, -1):
    sleep(1)
    print (c)
print ('Feliz ano novo!')
