#escreva um programa que leia dois numeros inteiros e compare-os.
#o 1 numero é maior ou o 2 numero é maior ou se são iguais

primeiro = int(input('Digite um numero para comparação: '))
segundo = int(input('Digite o segundo numero para comparação: '))

if primeiro > segundo:
    print(f'O primeiro numero ({primeiro}) é maior que o segundo ({segundo}).')
elif primeiro == segundo:
    print ('Ambos os numeros são iguais.')
else:
    print (f'O segundo numero ({segundo}) é maior que o primeiro número ({primeiro}).')