import random
rodadas = 1
#Lógica para Definir Jogadas
for rodadas in range(rodadas):
    print('Vamos começar!')
    jogada1 = int(input('Escolha sua jogada: (1) Pedra (2) Papel (3) Tesoura: '))
    if jogada1 == 1:
        jogada1 = "Pedra"
    elif jogada1 == 2:
        jogada1 = "Papel"
    elif jogada1 == 3:
        jogada1 = "Tesoura"
    else:
        jogada1 = None
        print('Escolha um número entre 1 e 3')
        break
    print('Você jogou {}'.format(jogada1))
    jogada2 = (random.randrange(1,4))
    if jogada2 == 1:
        jogada2 = "Pedra"
    elif jogada2 == 2:
        jogada2 = "Papel"
    elif jogada2 == 3:
        jogada2 = "Tesoura"
    print('O Adversario jogou {}'.format(jogada2))

