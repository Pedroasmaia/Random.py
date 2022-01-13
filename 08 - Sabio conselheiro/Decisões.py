import random
from typing import Counter

#Variaveis para falas do sabio
y_falas = ['Acho que deveria', 'Quase sempre o mais certo é fazer','Vai dar certo', 'A decisão certa sempre é a mais improvavel','nunca fique a merce de sí mesmo', 'Não,seja cauteloso','Sim, apenas seja cauteloso']
n_falas = ['Então saia da minha frente','Em você vejo quão tolo um ser humano pode ser','Não se deve jogar joias para porcos','Não foi pra isso que me codaram','Sou eu quem resposto, ou alguem predestinou essa conversa?','Porque veio aqui então?']



print('Olá, eu sou o grande sabio Pyton da mongolia, que um conselho sobre o que fazer?')
print('Digite (1) para sim e (2) para não')


next = int(input())
if next == 1:
    print('Faça sua pergunta:')
    input()
    print(random.choice(y_falas))
elif next == 2:
    print(random.choice(n_falas))
else:
    print('Sabe conversar? É só dizer 1 ou 2')
#for qtd in range(qtd):