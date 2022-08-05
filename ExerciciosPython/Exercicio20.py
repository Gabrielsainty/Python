#O mesmo professor do desafio anterior quer sortear a ordem de apresentacao dos trabalhos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random

aluno1 = input('Qual o nome do 1º aluno? ')
aluno2=input('Qual o nome do 2º aluno? ')
aluno3=input('Qual o nome do 3º aluno? ')
aluno4=input('Qual o nome do 4º aluno? ')
lista = [aluno1, aluno2, aluno3, aluno4]
#random.shuffle(lista)
#Neste exemplo, mudei de shuffle para sample, pois ai a lista permanece imutavel, e ainda consigo o resultado desejado.
print ('A ordem de apresentação será {}.'.format(random.sample(lista, 4))) #o 4 apos o () é pra indicar a quantidade limite de escolhas
