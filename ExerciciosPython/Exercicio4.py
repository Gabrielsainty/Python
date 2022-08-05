#Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informações possiveis sobre ele. 
# No caso seria um teste pra ler os parametros dos .isxxxx

teste = input('Digite aqui algo pertinente, gafanhoto...: ')
print ('Voce escreveu o tipo: ',type(teste))
print ('Aqui tem letras?',teste.isalpha())
print ('Aqui tem numeros?',teste.isnumeric())
print ('Aqui tem alfanumerico?',teste.isalnum())
print ('Aqui tem espaços?',teste.isspace())
print ('Aqui tem letras em caixa alta?',teste.isupper())
print ('Aqui tem letras em caixa baixa',teste.islower())
print ('Aqui tem valores ASCII?',teste.isascii())
print ('Aqui tem valores ASCII?',teste.istitle())