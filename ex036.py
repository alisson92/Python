casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? ')) # anos vezes 12
prestação = casa / (anos*12)
limite = (salário*30)/100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestação))
if (prestação > limite):
    print('Empréstimo \033[1;31;40mNEGADO\033[m!')
else:
    print('Empréstimo \033[1;32;40mACEITO\033[m!')

