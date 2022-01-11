from random import choice
n1 = str(input('O primeiro Aluno: '))
n2 = str(input('O segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O escolhido foi: {} '.format(escolhido))
