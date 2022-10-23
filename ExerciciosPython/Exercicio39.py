#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua nasc: 
#Se ele ainda ira se nascar no Serviço Militar obrigatorio
#Se é a hora de se nascar
#Se já passou do tempo do seu alistament
#Seu programa também deverá mostrar o tempo que passou do prazo.

ano = int(2022)
nasc = int(input('Fale qual o ano de nascimento: '))

if nasc == 18:
    print ('Você devera comparecer ao alistamento ainda esse ano.')
elif nasc > 18:
    print (f'Você já compareceu ao alistamento obrigatório à {abs(ano-nasc)} anos.')
else:
    print('Voce ainda deve comparecer ao alistamento Obrigatorio.')

    abs()