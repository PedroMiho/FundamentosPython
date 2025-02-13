# Desafio 01
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade = int(input("Digite sua velocidade em KM/h: "))

limiteVelocidade = 80

if velocidade > limiteVelocidade:
    # opção 1
    velocidadeUltrapassada = velocidade - limiteVelocidade
    valorPagar = velocidadeUltrapassada * 7
    
    # opção 2
    multa = (velocidade - limiteVelocidade) * 7
    print(f"Você foi multado em R$ {multa:.2f}")
    
else:
    print("Você não foi multado")