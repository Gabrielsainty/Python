#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas as letras minusculas
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = 'Princesinha do Funk umdoistres'
print (f'O nome a ser analisado é {nome}.')
print (f'Ele todo em maiúsculo é {nome.upper()}.')
print (f'Ele todo em minusculo é {nome.lower()}.')
print (f'A quantidade de caracteres sem espaços é igual a {len(nome.strip())}.')
print (f'A quantidade de letras que tem o primeiro nome é {len(nome.split()[0])}.')
