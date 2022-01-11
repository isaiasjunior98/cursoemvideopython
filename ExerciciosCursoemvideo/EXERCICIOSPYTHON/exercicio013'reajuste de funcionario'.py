salario = float(input('Qual é o salario do funcionário? R$'))
por = float(input('Qual é a porcentagem de reajuste? :'))
rea = salario*por/100
rea1 = rea+salario
print('O salario R${} com o reajuste de {}% é {:.2f}'. format(salario, por, rea1))
