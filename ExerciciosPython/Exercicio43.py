#Desenvolva uma logica que leia um peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

#abaixo de 18.5: Abaixo do peso1
#entre 18.5 e 25: peso normal
#entre 25 e 30: acima do peso
#entre 30 e 40: obesidade2
#acima de 40: obesidade morbida1
print ('==--' * 20)
print (' '*30 + 'CALCULADORA DE IMC')
print ('==--' * 20)
peso = float(input('Por favor, digite seu peso para calcularmos seu IMC: '))
alt = (float(input('Por favor, agora digite sua altura: '))**2)

IMC = peso / alt 

if IMC >= 40:
    print (f'Seu IMC deu {IMC:.1f}. Voce está dentro da faixa de obesidade mórbida, e é um risco para sua vida! O ideal seria procurar um profissional para acompanhar uma rotina de exercícios e alimentação regrada.')

elif IMC >= 30:
    print(f'Voce está obeso, procure realizar uma dieta unida á prática de exercícios físicos. ({IMC:.1f})')

elif IMC >= 25:
    print (f'Voce está acima do peso. Procure observar melhor suas refeições e manter uma alimentação saudável. ({IMC:.1f})')

elif IMC >= 18.5:
    print(f'Voce está dentro de seu peso ideal! ({IMC:.1f}).')

elif IMC < 18.5:
    print (f'Voce está abaixo do peso. Consulte um profissional para lhe passar uma orientação para se alimentar melhor.({IMC:.1f})')