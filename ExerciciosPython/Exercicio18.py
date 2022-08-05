#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math

angl = float(input('Qual o valor do angulo? '))

seno = math.sin(math.radians(angl))

cosseno = math.cos(math.radians(angl))

tangente = math.tan(math.radians(angl))

print (f'O ângulo {angl}, tem o seno de valor:{seno:.3f}, cosseno de valor:{cosseno:.3f} e tangente de valor:{tangente:.3f}.')

'''Vale destacar que quando voce utilizar muitas referencias a um modulo, voce pode limpar o codigo importanto diretamente as que se repetem
nesse exemplo, daria pra importar de math: sin,cos,tan e radians'''