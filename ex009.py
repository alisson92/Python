# Fazer uma tabuada

num = int(input('Digite um número para ver sua tabuada: '))
cont = 0
print('================')
for (cont) in range(0, 10):
    cont = cont + 1
    res = num * cont
    print('{} x {:2} = {}' .format(num, cont, res))
print('================')