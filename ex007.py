# Desenvolver um programa que leia as duas notas
# de um aluno, calcule e mostre a sua média.

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('A soma da nota {} mais a nota {}, equivale a média {}.' .format(nota1, nota2, media))
