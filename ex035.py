print('-='*40)
print('Analisador de Triângulos')
print('-='*40)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
maior = a
if ((a-b) < c) and (c < (a+b)):
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')