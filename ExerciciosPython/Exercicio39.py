#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua nasc: 
#Seu programa também deverá mostrar o tempo que passou do prazo.
from datetime import date

atual = date.today().year

sexo = input('Me diga qual seu sexo: ')
if sexo == 'mulher' and 'Mulher' and 'MULHER':
    print ('Mulheres não possuem obrigatoriedade de alistamento.')
    quit
else:
    print('Homens necessitam se alistar quando fizerem 18 anos.')
nasc = int(input('Me diga qual o ano de seu nascimento: '))
idade = atual - nasc
maior = idade - 18
menor = 18 - idade
print (f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print ('Você devera comparecer ao alistamento ainda esse ano.')
elif idade > 18:
    print (f'Você já compareceu ao alistamento obrigatório à {maior} anos.')
elif idade < 18:
    print(f'Ainda faltam {menor} anos para o alistamento obrigatorio.')