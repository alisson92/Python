peso = float(input('Qual é o seu peso? (Kg): '))
altura = float(input('Qual é a sua altura? (m): '))
imc = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if (imc < 18.5):
    print('Você está ABAIXO DO PESO normal')
elif (imc >= 18.5) and (imc < 25):
    print('PARABÉNS!! Você está na faixa de PESO IDEAL')
elif (imc < 30):
    print('Você está com um pouquinho de SOBREPESO. Dê uma maneirada!')
elif (imc < 40):
    print('Você está em OBESIDADE')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')