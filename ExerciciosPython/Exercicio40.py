#Crie um programa que leia duas notas do aluno e leia sua media e responda uma mensagem no final com sua media

med1 = float(input('Digite a média de portugues: '))
med2 = float(input('Digite a média de matematica: '))

medt = (med1 + med2) / 2

if medt == 10:
    print (f'A sua média foi {medt:.2f}.Parabéns, voce conseguiu a pontuação máxima')
elif medt >= 7:
    print(f'A sua média foi {medt:.2f}.Está indo muito bem, continue assim!')
elif medt >= 5:
    print(f'A sua média foi {medt:.2f}.Passou de raspão, a média precisa melhorar senão terá problemas!')
else:
    print (f'A sua média foi {medt:.2f}.A sua média está pessima, estude o quanto antes!')