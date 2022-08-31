distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.' .format(distancia))
if (distancia <=200):
    preço = 0.50 * distancia
else:
    preço = 0.45 * distancia
print('E o preço da sua passagem será de R${:.2f}' .format(preço))
