primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))
if (primeiro > segundo):
    maior = primeiro
    print('O PRIMEIRO valor é maior')
elif (primeiro < segundo):
    maior = segundo
    print('O SEGUNDO valor é maior')
elif (primeiro == segundo):
    print('Os dois valores são IGUAIS')