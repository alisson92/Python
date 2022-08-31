real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.73
euro = real / 5.07
libra = real / 5.95
iene = real * 27.30
print('Com R${:.2f} você pode comprar US${:.2f}, €{:.2f} £{:.2f}, ¥{:.2f}' .format(real, dolar, euro, libra, iene))