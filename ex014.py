# conversor de temperatura de celsius para farenheit

temp = float(input('Informe a temperatura em ºC: '))
faren = ((temp * 9) / 5) + 32
print('A temperatura de {}ºC corresponde a {}ºF!' .format(temp, faren))