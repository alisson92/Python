from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
sexo = str(input('Qual o seu sexo? '))
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if (sexo == 'masculino'):
    if (idade > 18):
        alistar = idade - 18
        convocado = atual - alistar
        print('Você já deveria ter se alistado há {} anos.'.format(alistar))
        print('Seu alistamento foi em {}'.format(convocado))
    elif (idade < 18):
        alistar = 18 - idade
        convocado = atual + alistar
        print('Ainda faltam {} anos para o alistamento'.format(alistar))
        print('Seu alistamento será em {}'.format(convocado))
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')
else:
    print('Você é do sexo {} e não é OBRIGADA a se alistar!'.format(sexo))