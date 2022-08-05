#um professor quer sortear um de seus quatro alunos parar apagar o quadro. Faça um programa que ajude ele, lendo os nomes dos alunos
# e escrevendo o nome do escolhido.

from random import choice
aluno1 = input('Qual o nome do 1º aluno? ')
aluno2=input('Qual o nome do 2º aluno? ')
aluno3=input('Qual o nome do 3º aluno? ')
aluno4=input('Qual o nome do 4º aluno? ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)

print(f'O aluno escolhido foi {escolhido}!')