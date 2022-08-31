soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if (num % 2 == 0):
        cont += 1
        soma += num
print('Foram digitados {} número pares. A soma de todos os pares é {}'.format(cont,soma))