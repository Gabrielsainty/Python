#Jogo de Pergunta e Resposta
#
print ('Bem vindo ao pequeno jogo que estou testando em Python!')
jogar = input('Você deseja jogar?' )
if jogar.lower() == 'sim':
    print ('Perfeito! O jogo é um quiz, e cada resposta correta vale um ponto. Vamos lá:')
else:exit()

score = 0

pergunta1 = input ('Como se chama o fenômeno que envolve a refração da luz que é apreciado por todos? ')
pergunta1.lower()
if pergunta1 != 'arcoiris': #Eu poderia colocar .lower() na frente da classe aqui para retornar as respostas sempre em caixa baixa/alta, para minimizar erros de digitação em caso de resposta certa.
    print ('Sinto muito, resposta errada! Mais sorte da próxima vez')
else: print ('Parabéns,voce conseguiu um ponto!')
score += 1 #Importante frisar que o simbolo é o sinal desejado na frente do sinal de =

pergunta2 = input ('Qual o nome técnico do USB em ingles? ')
pergunta2.lower()
if pergunta2 != 'universal serial bus':
    print ('Sinto muito, resposta errada! Mais sorte da próxima vez')
else: print ('Parabéns,voce conseguiu mais um ponto!')
score += 1

pergunta3 = input ('Como se chama o agente responsável pela troca térmica que ocorre na superfície da CPU? ')
pergunta3.lower()
if pergunta3 != 'pasta termica':
    print ('Sinto muito, resposta errada! Mais sorte da próxima vez')
else: print ('Parabéns,voce acertou todas as perguntas!')
score += 1

print ('Voce conseguiu {} pontos!'.format(score))
print ('Voce acertou {}%.'.format((score / 3) * 100))
