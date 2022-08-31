# Criar um algoritmo que leia um número e mostre
# o seu dobro, o seu triplo e a raiz quadrada.

n1 = int(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1**(1/2)
print('O dobro de {} é {}, seu triplo é {}, e sua raiz quadrada é {}.' .format(n1, dobro, triplo, int(raiz)))