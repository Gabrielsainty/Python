import random
from time import sleep

jogo = str(input('Deseja jogar Jokenpô comigo?? '))
if jogo.lower == 'sim':
    print('Beleza, então vamos lá!')
else:
     quit()
escolhas = ['pedra','papel','tesoura']
opt2 = random.randint(0,2)
print (f'O computador escolheu {escolhas[opt2]}')

print ('[0] Pedra \n[1] Papel \n[2] Tesoura')
opt1 = int(input('Qual das opções você escolhe? '))

sleep(1)
print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print('PO')


if opt1 == 0 and opt2 == 0:
    print ('EMPATE!')
    print (f'Voce escolheu {escolhas[0]} e o computador escolheu {escolhas[opt2]}!')

if opt1 == 0 and opt2 == 1:
    print ('VOCE PERDEU!')
    print (f'Voce escolheu {escolhas[0]} e o computador escolheu {escolhas[opt2]}!')

if opt1 == 0 and opt2 == 2:
    print ('VOCE GANHOU!')
    print (f'Voce escolheu {escolhas[0]} e o computador escolheu {escolhas[opt2]}!')

if opt1 == 1 and opt2 == 0:
    print ('VOCE GANHOU!')
    print (f'Voce escolheu {escolhas[1]} e o computador escolheu {escolhas[opt2]}!')

if opt1 == 1 and opt2 == 1:
    print ('EMPATE!')
    print (f'Voce escolheu {escolhas[1]} e o computador escolheu {escolhas[opt2]}!')

if opt1 == 1 and opt2 == 2:
    print ('VOCE PERDEU!')
    print (f'Voce escolheu {escolhas[1]} e o computador escolheu {escolhas[opt2]}!')

if opt1 == 2 and opt2 == 0:
    print ('VOCE PERDEU!')
    print (f'Voce escolheu {escolhas[2]} e o computador escolheu {escolhas[opt2]}!')

if opt1 == 2 and opt2 == 1:
    print ('VOCE GANHOU!')
    print (f'Voce escolheu {escolhas[2]} e o computador escolheu {escolhas[opt2]}!')

if opt1 == 2 and opt2 == 2:
    print ('EMPATE!')
    print (f'Voce escolheu {escolhas[2]} e o computador escolheu {escolhas[opt2]}!')