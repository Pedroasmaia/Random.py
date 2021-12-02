goleiros = []
zagueiros = []
laterais = []
meias = []
atacantes = []

print('Quantos goleiros seu time vai ter?')
gol_qtd =  int(input())

if gol_qtd <= 3:
    for gol_qtd in range(gol_qtd):
        print('Escolha seu {}° Goleiro:'.format(gol_qtd + 1))    
        goleiros.append(input())
    print(goleiros)
elif gol_qtd == 0:
    print('Seu time deve ter no minimo 1 Goleiro')
else:
    print('Seu time pode ter no máximo 3 Goleiros')

print('Quantos zagueiros seu time vai ter?')
zag_qtd =  int(input())

if zag_qtd >= 2:
    for zag_qtd in range(zag_qtd):
        print('Escolha seu {}° Zagueiro'.format(zag_qtd + 1))
        zagueiros.append(input())
    print(zagueiros)
elif zag_qtd <= 1:
    print('Seu time deve ter no minimo 2 Zagueiros')
elif zag_qtd >= 6:
    print('Seu time pode ter no máximo 5 Zagueiros')

#print('Quantos meias seu time vai ter?')
#qtd_meias =  int(input())
#print('Quantos atacantes seu time vai ter?')
#qtd_atacantes =  int(input())