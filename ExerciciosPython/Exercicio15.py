#Escreva um programa que pergunte a quantidade de Kms percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60$ por dia e 0,15$ por km rodado.

dia = float(input('Quantos dias você utilizou o veiculo? '))
kms = float(input('Quantos kms você percorreu? '))
pago = (kms * 0.15) + dia * 60
#pkms = kms * 0.15 Percebi que dava pra otimizar no meio da aula do guanabara.
#pdia = dia * 60
aluguel = print(f'O custo total do aluguel é R${pago:.2f}.')