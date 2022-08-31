print('\033[32;40m-=\033[m'*35)
print('\033[;1;31;40mAnalisador de Triângulos v2.0\033[m')
print('\033[32;40m-=\033[m'*35)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    if (a == b) and (b == c):
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    elif (a == b) and (a != c) or (a == c) and (a != b) or (b == c) and (b != a):
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
    elif (a != b) and (b != c) and (c != a):
        print('Os segmentos acima PODEM FORMAR um trinângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')