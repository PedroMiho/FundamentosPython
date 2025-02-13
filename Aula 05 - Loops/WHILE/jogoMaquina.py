import random

maquina = random.randint(0 , 10)

while True:
    usuario = int(input("Digite um numero: "))
    
    if maquina == usuario:
        print("ACERTOU")
        break