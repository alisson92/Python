# Calcular o preço de aluguel de carros

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
aluguel = (km * 0.15) + (60 * dias)
print('O total a pagar é de R${:.2f}' .format(aluguel))