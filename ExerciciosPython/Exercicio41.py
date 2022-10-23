#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#ate 9 anos MIRIM
#ate 14 anos INFANTIL
#ate 19 anos JUNIOR
#ate 20 anos SENIOR
#acima MASTER
nasc = int(input('Por favor, digite o ano de nascimento: '))
idade = 2022 - nasc

if idade <= 9:
    print (f'Para alunos de {idade}, a categoria que ele pertence é MIRIM')
elif idade <= 14:
    print (f'Para alunos de {idade}, a categoria que ele pertence é INFANTIL')
elif idade <= 19:
    print (f'Para alunos de {idade}, a categoria que ele pertence é JUNIOR')
elif idade <= 20:
    print (f'Para alunos de {idade}, a categoria que ele pertence é SENIOR')
else:
    print (f'Para alunos de {idade}, a categoria que ele pertence é MASTER')