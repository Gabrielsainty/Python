import random

limite = input('Escolha até que numero a máquina pode calcular: ')

if limite.isdigit():
    limite = int(limite)

    if limite <= 0:
        print ('Não tente me enganar com números negativos =D.')
        quit()
else: 
    print ('Usar palavras não vale, pare de roubar pelo amor de Deus!.')
    quit()

aleatorio = random.randint(0, limite)
print (aleatorio)  #esse comando é pra saber o valor pra testar as funções, reative ele

while True:
    adivinhado = input('Adivinhe qual numero é: ')
    if adivinhado.isdigit():
        adivinhado = int(adivinhado)

    else: 
        print ('Ainda tentando me enganar com letras?? Voce é melhor do que isso...')
        continue

    if adivinhado == aleatorio:
            print ('Monstruoso, voce acertou! =D')
            break
    else:
        print ('Que pena, voce errou! =z')