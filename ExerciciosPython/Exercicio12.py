#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com alguma % de desconto

produto = float(input('Qual o preço do produto que deseja no mercado?'))
desconto= float(input('Qual o valor do desconto que encontrou?'))
promo = produto*desconto/100
print (f'A promoção do mercado reduziu o preço do produto em {desconto}% e passou a custar {produto-promo}')