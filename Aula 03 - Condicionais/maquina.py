#Jogo Maquina 
# Maquina gerar um numero aletorio entre (0 a 5)
# Usuario vai tentar acertar o numero

import random

maquina = random.randint(0,5)
print(maquina)

usuario = int(input("Digite um número entre 0 a 5: "))

# IF - Operador de Comparação

if maquina == usuario:
    print("Acertou")
else:
    print("Errou")