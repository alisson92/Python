salário = float(input('Qual o salário do funcionário? R$'))
if (salário > 1250.00):
    nsalário = salário + (salário*10/100)
if (salário <= 1250.00):
    nsalário = salário + (salário*15/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.' .format(salário, nsalário))