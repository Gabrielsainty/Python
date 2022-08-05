#Desenvolva um programa que pergunte a distancia da viagem em kms, calcule o preço da passagem de onibus cobrando:
#R$0,50 por km para viagens até 200kms e R$0,45 para viagens maiores que isso
distv = float(input('Qual a distância da viagem que você quer realizar? '))
ticket = distv * 0.5 if distv <= 200 else distv * 0.45
#print(f'O preço da passagem vai sair a R${ticket} por ser uma viagem menor que 200 kms.'),print('Considere realizar viagens mais longas pra aproveitar nosso desconto!') if distv <= 200 else print (f'O preço da passagem vai sair a R${ticket} por ser uma viagem maior que 200 kms.'),print ('Obrigado por aproveitar nosso preço promocional para viagens longas!')
if distv <= 200:
    ticket = distv * 0.5 if distv <= 200 else distv * 0.45
    print (f'O preço da passagem vai sair a R${ticket} por ser uma viagem menor que 200 kms.')
    print ('Considere realizar viagens mais longas pra aproveitar nosso desconto!')
else:
    ticket = distv * 0.45
    print (f'O preço da passagem vai sair a R${ticket} por ser uma viagem maior que 200 kms.')
    print ('Obrigado por aproveitar nosso preço promocional para viagens longas!')