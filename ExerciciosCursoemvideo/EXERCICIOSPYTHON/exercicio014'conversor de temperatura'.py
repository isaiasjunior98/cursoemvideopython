temp = float(input('Qual a temperatura ºC? '))
fah = temp*1.8 + 32
celsius = fah-32
celsius2 = celsius/1.8
print('A temperatura {}ºC é {}Fº'.format(temp, fah))
print('A temperatura {}Fº é {}ºC'.format(fah, celsius2))
