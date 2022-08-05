#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.

speed = int(input('Qual a velocidade que foi avistado o carro? '))

if speed > 80:
    excesso = speed - 80
    multa = excesso * 7
    print (f'Então com certeza ele foi multado, e ainda vai ter que pagar R${multa:.2f} de multa. Ta lascado...')
else:
    print ('Ah, então estava dentro da velocidade permitida, que bom!')