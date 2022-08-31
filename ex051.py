print('='*30)
print(' 10 TERMOS DE UMA PA')
print('='*30)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
for c in range(0, 10):
    print(termo, end=' ')
    termo += razão
print('ACABOU')