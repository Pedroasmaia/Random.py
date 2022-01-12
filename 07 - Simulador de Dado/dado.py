import random
print('Quantas jogadas você quer realiza?')
#Jogar o dado quantas vezes?
jogadas = int(input())
for jogadas in range(jogadas):
#Rodar o dado com um numero aleatorio de 1 a 6
    valor = random.randrange(1,7)
    print('O Resultado da sua {}° foi : {}'.format(jogadas + 1,valor))