vel = float(input('Qual a velocidade do carro? '))
if (vel <= 80):
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = 7 * (vel - 80)
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!' .format(multa))
    print('Tenha um bom dia! Dirija com segurança!')