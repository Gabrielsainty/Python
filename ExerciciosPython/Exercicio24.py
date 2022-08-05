#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO".

pergunta = (input('Digite o nome de uma cidade: '))
cid = pergunta.upper()
temounao = cid.startswith('SANTO')
print (temounao)