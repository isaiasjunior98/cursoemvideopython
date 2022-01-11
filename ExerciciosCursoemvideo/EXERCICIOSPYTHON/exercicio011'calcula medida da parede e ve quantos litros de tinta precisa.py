par = float(input('Qual a largura da parede?: '))
alt = float(input('Qual a altura da parede? : '))
area = par * alt
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é {}m²!'. format(par, alt, area))
print('Você precisará de {:.2f} litros de tinta!'.format(tinta))
