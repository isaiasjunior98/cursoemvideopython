a1 = float(input('Quantos dias alugados? : '))
a2 = float(input('Quantos Km rodados? : '))
custodia = a1*60
custokm = a2*0.15
a3 = custodia + custokm
print('O valor a ser pago é R${:.2f}!'.format(a3))
