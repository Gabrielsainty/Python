#Crie um programa que leia quanto din uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
din = float(input('Quanto voce tem na carteira atualmente? '))
conv=3.27
dol=float(din/conv)
print (f'Com R${din:.3} eu consigo comprar U${dol:.3} dolares na agência de câmbio')
