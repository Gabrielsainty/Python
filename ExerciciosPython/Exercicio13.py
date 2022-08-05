#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
#
funn = input('Qual o nome do funcionário? ')
funs = int(input('Qual o salário do funcionario? R$'))
funa = int(input('Ele teve um aumento de quantos %?'))
aumento = int(funs*15/100)
print (f'O funcionário {funn} recebeu {funa} de aumento e agora receberá {aumento}, sendo agora {funs+aumento}')
#print ('O funcionário Adalberto recebeu 15% de aumento e agora receberá {}'.format(funs*15/100== FuncBonus))
#print (f'O salário de Adalberto agora é {FuncBonus}')

#print ('O funcionário Adalberto recebeu 15% de aumento e agora receberá {}'.format(funs*15/100== FuncBonus)) 