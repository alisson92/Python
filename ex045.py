import random
from time import sleep
opção = 'Pedra', 'Papel', 'Tesoura'
computador = random.choice(opção)
print('\033[32;40m========== \033[;4;32;40mJ O K E N P O \033[;32;40m==========\033[m')
print('\033[;1;31;40mVamos jogar?\033[m')
print('''\033[;1;97;40mSuas opções são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if (jogador == 0):
    jogador = 'Pedra'
elif (jogador == 1):
    jogador = 'Papel'
elif (jogador == 2):
    jogador = 'Tesoura'
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*15)
print('Jogador jogou {}'.format(jogador))
print('Computador jogou {}'.format(computador))
print('-='*15)
sleep(0.8)
print('Carregando resultado...')
sleep(1)
if (jogador == 'Pedra') and (computador == 'Pedra') or (jogador == 'Papel') and (computador == 'Papel') or (jogador == 'Tesoura') and (computador == 'Tesoura'):
    print('EMPATE')
elif (jogador == 'Pedra') and (computador == 'Papel'):
    print('COMPUTADOR VENCE!')
elif (jogador == 'Pedra') and (computador == 'Tesoura'):
    print('JOGADOR VENCE!')
elif (jogador == 'Papel') and (computador == 'Pedra'):
    print('JOGADOR VENCE!')
elif (jogador == 'Papel') and (computador == 'Tesoura'):
    print('COMPUTADOR VENCE!')
elif (jogador == 'Tesoura') and (computador == 'Papel'):
    print('JOGADOR VENCE!')
elif (jogador == 'Tesoura') and (computador == 'Pedra'):
    print('COMPUTADOR VENCE!')