goleiros = []
zagueiros = []
laterais = []
meias = []
atacantes = []

print('Quantos goleiros seu time vai ter?')
qtd_goleiros =  int(input())

if qtd_goleiros <= 3:
    for qtd_goleiros in range(qtd_goleiros):
        print('Escolha seu {}° Goleiro:'.format(qtd_goleiros + 1))    
        goleiros.append(input())
    print(goleiros)
elif qtd_goleiros == 0:
    print('Seu time deve ter no minimo 1 Goleiro')
else:
    print('Seu time pode ter no máximo 3 Goleiros')
    print(goleiros)




#print('Quantos zagueiros seu time vai ter?')
#qtd_zagueiros =  int(input())
#print('Quantos meias seu time vai ter?')
#qtd_meias =  int(input())
#print('Quantos atacantes seu time vai ter?')
#qtd_atacantes =  int(input())