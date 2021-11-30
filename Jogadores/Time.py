goleiros = []
zagueiros = []
laterais = []
meias = []
atacantes = []

print('Quantos goleiros seu time vai ter?')
qtd_goleiros =  int(input())
print('Quantos zagueiros seu time vai ter?')
qtd_zagueiros =  int(input())
print('Quantos meias seu time vai ter?')
qtd_meias =  int(input())
print('Quantos atacantes seu time vai ter?')
qtd_atacantes =  int(input())

if qtd_goleiros > 3:
    print("Escolha no máximo 3 goleiros")