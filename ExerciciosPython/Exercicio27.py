#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite o seu primeiro e último nome: ')
nseparado = nome.split()
#print (f'Então seu primeiro nome é {nseparado[0]} e seu segundo nome é {nseparado[len(nseparado)-1]}') usando o len
print (f'Então seu primeiro nome é {nseparado[0]} e seu ultimo nome é {nseparado[-1]}') #usando a lista com ordem invertida