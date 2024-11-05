import random
from time import sleep

# BANCO DE DADOS

lista = ["\U0001F929", "\U0001F439", "\U0001F430", "\U0001F43C", "\U0001F42F", "\U0001F437", "\U0001F438", "\U0001F992", "\U0001F427"]

moedas = int(2000)

# INICIALIZAÇÃO

print('-=-'*25)

print(f'{"BEM VINDO AO JOGO DO TIGRÃO":^75}')
print(f'{"VOCÊ COMEÇA COM 2.000 MOEDAS E CADA RODADA CONSOME 100":^75}')
print(f'{"CASO VOCÊ VENÇA NA HORIZONTAL GANHARÁ 500 MOEDAS":^75}')
print(f'{"CASO VENÇA NA VERTICAL GANHARÁ 500 MOEDAS":^75}')
print(f'{"SE CONSEGUIR VENCER NA DIAGONAL RECEBERÁ 1.000 MOEDAS":^75}')

print('-=-'*25)
sleep(2)
jogador = float(input(f'{"PARA JOGAR APERTE 1 E PARA PARAR DE JOGAR APERTE 0: ":^75}'))
sleep(2)
print('-=-'*25)

# JOGO


while moedas > 0  and  jogador !=0 :
    moedas = moedas -100
    
    sleep(1)

    n1 = random.choice(lista)
    n2 = random.choice(lista)
    n3 = random.choice(lista)
    n4 = random.choice(lista)
    n5 = random.choice(lista)
    n6 = random.choice(lista)
    n7 = random.choice(lista)
    n8 = random.choice(lista)
    n9 = random.choice(lista)

    print('''
                              [{}] [{}] [{}]
                              [{}] [{}] [{}]
                              [{}] [{}] [{}]'''.format(n1,n2,n3,n4,n5,n6,n7,n8,n9))
    print('\n')
    
    if n1 == n2 == n3:
        print ('VOCÊ GANHOU NA PRIMEIRA HORIZONTAL')
        moedas = moedas +500
        print ('SUAS MOEDAS ATUAIS SÃO DE {}'.format(moedas))

    elif n4 == n5 == n6:
        print('VOCÊ GANHOU NA SEGUNDA HORIZONTAL')
        moedas = moedas +500
        print ('SUAS MOEDAS ATUAIS SÃO DE {}'.format(moedas))

    elif n7 == n8 == n9:
        print ('VOCÊ GANHOU NA TERCEIRA HORIZONTAL')
        moedas = moedas +500
        print ('SUAS MOEDAS ATUAIS SÃO DE {}'.format(moedas))

    elif n1 == n5 == n9 or n3 == n5 == n7:
        print ('PARABÉNS VOCÊ GANHOU NA DIAGONAL')
        moedas = moedas +1000
        print ('SUAS MOEDAS ATUAIS SÃO DE {}'.format(moedas))

    elif n1 == n4 == n7:
        print ('VOCÊ GANHOU NA PRIMEIRA VERTICAL')
        moedas = moedas +500
        print ('SUAS MOEDAS ATUAIS SÃO DE {}'.format(moedas))

    elif n2 == n5 == n8:
        print('VOCÊ GANHOU NA SEGUNDA VERTICAL')
        moedas = moedas +500
        print ('SUAS MOEDAS ATUAIS SÃO DE {}'.format(moedas))

    elif n3 == n6 == n9:
        print('VOCÊ GANHOU NA TERCEIRA VERTICAL')
        moedas = moedas +500
        print ('SUAS MOEDAS ATUAIS SÃO DE {}'.format(moedas))

    else:
        print ('VOCÊ PERDEU!')
        print ('SUAS MOEDAS ATUAIS SÃO DE {}'.format(moedas))

    sleep(1)
    print('\n')

    jogador = float(input('QUER TENTAR NOVAMENTE?  '))


print('VOCÊ NÃO TEM MAIS MOEDAS PARA JOGAR!')












