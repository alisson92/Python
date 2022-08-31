print('\033[;1;31;40m============= LOJAS CORREA LIMA =============\033[m')
compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if (opção == 1):
    compras10 = compras - (compras * 10) / 100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compras, compras10))
elif (opção == 2):
    compras5 = compras - (compras * 5) / 100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compras, compras5))
elif (opção == 3):
    parcela = int(input('Quantas parcelas? '))
    if (parcela <= 2):
        compra2x = compras / parcela
        print('Sua compra será parcelada em {}x de R${:.2f} SEM JUROS'.format(parcela, compra2x))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compras, compras))
elif (opção == 4):
    parcela = int(input('Quantas parcelas? '))
    if (parcela >= 3):
        juros = (compras * 20) / 100
        compras3x = compras + (compras * 20) / 100
        valor_parcela = compras3x / parcela
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, valor_parcela))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compras, compras3x ))
else:
    print('OPÇÃO INVÁLIDA!!!')