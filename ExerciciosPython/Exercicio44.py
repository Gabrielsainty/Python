#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição do pagamento:
#A vista dinheiro/Cheque: 10% Off
#A vista no cartão: 5% off
#em até 2x no cartão: preço normal
#3x ou mais: 20% de juros

pp = float(input('Digite o preço do produto que deseja comprar:'))
opt = int(input('[ ] A Vista Dinheiro/Cheque \n[ ] A vista cartão \n[ ] 2x no cartão \n[ ] 3x ou mais no cartão \nQual metodo de pagamento irá utilizar: '))

if opt == 1:
    total = pp - (pp * 10 / 100)
    print (f'O produto custa R${pp:.2f} e terá direito a 10% de desconto, passando a custar R${total}.')

elif opt == 2:
    total = pp - (pp * 5 / 100)
    print (f'O produto custa R${pp:.2f} e terá direito a 5% de desconto, passando a custar R${total}.')

elif opt == 3:
    total = pp / 2
    print (f'O produto custará R${pp:.2f}, parcelado em 2x de {total:.2f} ,não tendo direito a descontos.')

elif opt == 4:
    parc = int(input('Em quantas vezes deseja parcelar: '))
    total = pp + (pp * 20 / 100)
    print (f'O produto custa R${pp:.2f}, parcelado em {parc}x, passando a custar R${total} de juros.')
    