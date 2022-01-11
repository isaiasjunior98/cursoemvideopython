p = float(input('Qual o valor do produto ? R$'))
d = p*5
d2= d/100
d3 = p - d2
print('O valor do produto é {}, na promoção de 5% vai custar {:.2f}! '.format(p, d3))
