número = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opção = int(input('Sua opção: '))
if (opção == 1):
    print('\033[;1;31;40m{}\033[m convertido para BINÁRIO é igual a {}'.format(número, format(número,'b')))
elif (opção == 2):
    print('\033[;1;31;40m{}\033[m convertido para OCTAL é igual a {}'.format(número, format(número, 'o')))
elif (opção == 3):
    print('\033[;1;31;40m{}\033[m convertido para HEXADECIMAL é igual a {}'.format(número, format(número, 'x')))
else:
    print('\033[;1;31;40mOPÇÃO INVÁLIDA. Tente novamente!!!\033[m')