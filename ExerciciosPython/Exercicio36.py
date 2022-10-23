#Crie um programa para aprovar um emprestimo bancario. Ele ira perguntar o valor da casa, o salário da pessoa e em quantos anos ela quer essa divida.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo sera negado.

valorcasa = float(input('Digite o valor da casa que quer adquirir: ')) #R$300000

valorsalario = float(input('Qual o seu salário atualmente: ')) #R$3000

qtdanos = int(input('Em quantos anos deseja realizar pagar esse emprestimo: ')) #20

qtdmeses = qtdanos * 12

limitedoemp = (valorsalario * 30) / 100
print (f'O valor máximo que voce pode pagar por empréstimo é de R${limitedoemp:.2f}')

if qtdanos <= 5:
    valoremprestimo = (valorcasa * 1.15)
    valordojuros = 15

if qtdanos <= 10:
    valoremprestimo = (valorcasa * 1.20) 
    valordojuros = 20

if qtdanos <= 15:
    valoremprestimo = (valorcasa * 1.25)
    valordojuros = 25

if qtdanos <= 20:
    valoremprestimo = (valorcasa * 1.30)
    valordojuros = 30

if qtdanos <= 25:
    valoremprestimo = (valorcasa * 1.35)
    valordojuros = 35

if qtdanos <= 30:
    valoremprestimo = (valorcasa * 1.40)
    valordojuros = 40

if qtdanos <= 35:
    valoremprestimo = (valorcasa * 1.45)
    valordojuros = 45

if qtdanos <= 40:
    valoremprestimo = (valorcasa * 1.50)
    valordojuros = 50

if qtdanos > 40:
    valoremprestimo = (valorcasa * 1.60)
    valordojuros = 60

#valoremprestimo = (valorcasa * 1.35)
parcelasemprestimo = valoremprestimo / qtdmeses

print (f'A casa que deseja comprar custa R${valorcasa:.2f}.')

print (f'O preço total do empréstimo contratado ficará em \033[4;31mR${valoremprestimo:.2f}\033[m, a ser pago em \033[4;31m{qtdmeses}\033[m meses, com taxa de juros de \033[4;31m{valordojuros}%\033[m o preço das parcelas do empréstimo será de \033[4;31mR${parcelasemprestimo:.2f}\033[m.')
if parcelasemprestimo < limitedoemp:
    print ('Esse empréstimo é permitido para você para contratação.')
else:
    print ('O valor do empréstimo excede o valor permitido de 30% do seu salário, portanto você não está autorizado a contratar.')