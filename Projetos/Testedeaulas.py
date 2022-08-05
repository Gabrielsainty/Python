'''int= 7, -4, 0, 9875
#float= 4.5, 0.076, -15.223, -7.0
#bool= True, False #A palavra tem que estar capitalizada.
#str= 'olá', 'como voce está?', '123456', '7.5',''#String vazia

#Definir qual a classe que sera usada dentro do print, pois por padrão ele sempre usa STR(string)

#n1 = int(input("Digite um numero:"))
#n2 = int(input("Digite mais um numero:"))
#s = n1+n2
#print("A soma entre {0}+{1} é igual á {2}".format(n1, n2, s))

#print(type(n1)) mostra graficamente qual o tipo que foi usado
#print("A soma vale{}".format(s)) serve pra represetar melhor valores dentro de uma linha str atraves da chave e format. 
#Exemplo: print("A soma entre {0}+{1} vale {2}".format(n1, n2, s))'''

#Aula 6 - Tipos primitivos e saida de dados
'''
int()  --> Para números inteiros ------------ 17, 21, 35, 42
float() -> Números de ponto flutuante ---2.3, 1.6, 14.9, -67.1
bool() --> Armazena True ou False --------True, False
str() ----> Conjunto de caracteres -------- 'complexo', 'coisinhadejesus', 'amistoso'
type() ---> Indica o tipo primitivo da var -  x = 'Sapo Tunado'   print(type(x)) logo seu tipo primitivo é string

teste = input('Digite aqui algo pertinente, gafanhoto...: ')
print ('Voce escreveu o tipo: ',type(teste))
print ('Aqui tem letras?',teste.isalpha())
print ('Aqui tem numeros?',teste.isnumeric())
print ('Aqui tem alfanumerico?',teste.isalnum())
print ('Aqui tem espaços?',teste.isspace())
print ('Aqui tem letras em caixa alta?',teste.isupper())
print ('Aqui tem letras em caixa baixa',teste.islower())
print ('Aqui tem valores ASCII?',teste.isascii())
print ('Aqui tem valores ASCII?',teste.istitle())'''

#Aula7 - Operadores Aritmeticos

'''+ = Adição  
- = Substração
= = Recebe 
/ = Divisão
* = Multiplicação
** = Potenciação
% = Resto da divisão
// = Divisão Inteira
5+2 == Adição  
5-2 == Substração
5=2 == Recebe 
5/2 == Divisão
5*2 == Multiplicação """Descobrir porque que #*, #*** ficam verdes e #% fica riscado"""
5**2 == Potenciação  
5%2 == Resto da divisão #Seria a prova real na matematica, quando vc vai descendo a lista com a quantidade de divisões possíveis daquele numero, só que esse aqui seria o resultado do resto
5//2 == Divisão Inteira #Seria a prova real na matematica, quando vc vai descendo a lista com a quantidade de divisões possíveis daquele numero, só que esse aqui seria o resultado das divisões

A Ordem de precedência dos simbolos vem 1=(), 2=**, 3=*,/,//,%, 4=+,- '''


'''Nome = input ('Qual o seu nome?')
print ('Prazer em te conhecer {}'.format(Nome))
print ('Prazer em te conhecer {:20}!É sempre bom ter você conosco! =D'.format(Nome))
Dentro do espaço {}, o ':' define a forma que sera construido a classe que vc usou ali, sendo que <,>,^ fazem o alinhamento nas direções correspondentes.
Inclusive colocar algo antes do alinhamento faz com que o espaço seja preenchido com esse caracter. (...conhecer {:=20} preencheria com simbolo = no caso.)
Ao colocar {:2f} por exemplo, voce declara que vai limitar a resposta a 2 casas, e o f declara que sera float, podendo ser f ou i ou s no caso então, falta testar.'''

'''l1 = int(input('Um valor: '))
l2 = int(input('Outro valor? '))
s=l1 + l2
d=l1 / l2
m=l1 * l2

print ('A soma vale {}, a multiplicação vale {} e a divisão vale {:4}'.format(s, m, d), end='')  #Caso queira quebrar a linha no meio do print, basta digitar \n
print ('Que loucura!') #o , end='' faz com que o proximo print siga na mesma linha, e a info dentro da aspa significa o que vira antes de continuar a proxima linha'''

#Aula 8 - Importar Modulos

'''Na hora de importar modulos, para trazer toda a classe é : import+xxxx (exemplo: import math)
Agora caso deseja importar um item especifico, o comando é: from+xxxx+import (exemplo:  from math import ceil,floor,etc)
Quando se importa o modulo todo, vc sempre tem que usar o comando precedente a formula (exemplo: raiz = math.sqrt)
Agora quando se importa apenas um item do modulo, nao e necessario usar o nome precedente. (exemplo: raiz = sqrt)'''

'''import math

num = int(input('Digite um numero por favor: '))
raiz = math.sqrt(num)
pot = math.pow(num)
print (f'A raiz quadrada de {num} é {raiz}')'''

'''Para utilizar listas, é só abrir uma chave e designar o nome, como se fosse igual aos parenteses. Ainda não sei se é 
necessario definir se pode ser int ou str dentro dessa lista'''

'''quando for criar uma lista e ter que escolher um item ou mais itens, existem as opções choice, choices e sample.
Choice retorna 1 escolha
Choices retorna qualquer item dentro da lista, com esse item podendo ser repetido
Sample retorna itens da lista, sem repetir.'''

#Aula 9 - Manipulando texto

'''Quando se cria uma string, o python permite que voce fatie a frase de algumas formas, a estrutura do fatiamento é: Variavel[x:x:x]
1º é o primeiro caracter da frase, 2º é o ultimo caracter da frase e o 3º é a frequencia em que sera mostrado.
No 1º, o digital representa exatamente o mesmo que voce indicou (exemplo, no nome Gabriel, o 1 caracter é o 'G', e ele mostraria o 'G')
No 2º, ele ira representar o caracter anterior ao ultimo (exemplo, no nome Gabriel, o 5 caracter é o 'i', então ele mostraria o 'r')
No 3º, ele irá indicar quantas casas deve-se pular (exemplo, no nome Gabriel, se fosse x:x:2 seria Gbil, e se fosse x:x:3 seria Grl)

funções que podem ser uteis para strings:
print (len(alfabeto))
print (alfabeto.find('rato'))
print (alfabeto.count('rato'))
print (alfabeto.replace('rato','bode'))
print (alfabeto.upper())
print (alfabeto.lower())
print (alfabeto.capitalize())
print (alfabeto.title())
print (alfabeto.startswith('rato','bode'))
print (alfabeto.strip()
print (alfabeto.lstrip())
print (alfabeto.rstrip())
print (alfabeto.split())
print (alfabeto.partition)
print ('-'.join(alfabeto))

para salvar alterações feitas a variavel, é necessário colocar '(variavel) = ' antes, caso contrario serão instancias de uso único, como para print.

alfabeto = 'O rato roeu a roupa do rei de roma'
alfabeto.split > Agora toda a frase(string) foi dividida em varias sentenças
separado = alfabeto.split() > Ele salvou a separação e criou uma nova variável
print (dividido[0]) > A variavel não é mais por letra, e sim por palavra que foi separada, no caso 0 seria 'O', 1 seria 'rato', 2 seria 'roeu'

na hora de usar listas (como quando usando variavel.split), todo numero positivo[0,1,2,3,...] começara na ordem normal, enquanto os 
negativos[-1,-2,-3,...] começaram do final em direção ao começo
'''

###USUARIO É A PIOR RAÇA QUE TEM, ELES SEMPRE IRÃO FAZER ALGO PRO SEU PROGRAMA PARAR DE FUNCIONAR###

#Aula 10 - Condições

'''carro = 'Automovel'

Num caminho reto
carro.siga()
carro.vireaesquerda()
carro.vireadireita()
carro.siga()
carro.vireadireita()
carro.siga()
carro.vireaesquerda()
carro.pare()

Num caminho com bifurcação
if carro.seguirdireita():
    bloco_T_
    carro.siga()
    carro.vireaesquerda()
    carro.vireadireita()
    carro.siga()
    carro.vireadireita()
    carro.siga()
    carro.vireaesquerda()
    carro.pare()
    
else: #carro.seguiresquerda():
    bloco_F_
    carro.siga()
    carro.vireaesquerda()
    carro.vireadireita()
    carro.siga()
    carro.siga()
    carro.pare()

QUANDO ELE POSSUI APENAS O IF, ENTÃO É UMA ESTRUTURA SIMPLES, MAS SE TIVER O ELSE VIRA UMA ESTRUTURA COMPOSTA

Versão Detalhada: 
tempo = int(input('Quantos anos tem seu carro?: '))
if tempo <= 5:
    print('Até que seu carro está novo...')
else:
    print('Essa caranga já ta só o pó da rabiola kkkk')

Versão Simplificada:
tempo = int(input('Quantos anos tem seu carro?: '))
print('Até que seu carro está novo...'if tempo <= 5 else print('Essa caranga já ta só o pó da rabiola kkkk'))'''

#EM ALGUNS COMANDO VOCE USARA == OU IS, MAS AMBOS TEM FUNCOES DIFERENTES.

#== SERVE PRA FUNÇÃO DE EQUALIDADE, PRA SABER SE O RESULTADO É O MESMO
#IS SERVE PRA FUNÇÃO DE REFERENCIA, PRA SABER SE AMBOS SE REFEREM AO MESMO OBJETO

#Aula 11 - Cores no Terminal

ANSI - Escape Sequence (American National Standards Institute )

\033[style;text;background;m #Esse é o padrão para criação de cores
# Um exemplo real de teste seria: print ('\033[1;37mOla Mundo!\033[1;37m') 
#a repetição dentro do print no final da frase é para não fazer com que a linha saia pintada até o final da tela.

#dentro do padrão style, alguns são: 0=Sem estilo; 1=Negrito; 4=Sobrelinhado;7=Negativo
#dentro do padrão texto, alguns são: 30=Branco 31=Vermelho 32=Verde 33=Amarelo 34=Azul claro 35=Rosa 36=Ciano 37=Cinza
#dentro do padrão background, alguns são: 40=Branco 41=Vermelho 42=Verde 43=Amarelo 44=Azul claro 45=Rosa 46=Ciano 47=Cinza
\033[0;30;41m