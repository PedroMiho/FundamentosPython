# Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem cobrando R$
# 0,50 por Km para viagens de até 200 Km e R$ 0,45 para
# viagens mais longas.

viagem = int(input("Digite a distancia: "))

if viagem <= 200:
    valor = 0.5 * viagem
    print(f"Valor a ser pago R$ {valor:.2f}")
else:
    valor = 0.45 * viagem
    print(f"Valor a ser pago R$ {valor:.2f}")
    
if viagem > 200:
    valor = 0.45 * viagem
    print(f"Valor a ser pago R$ {valor:.2f}")
else:
    valor = 0.5 * viagem
    print(f"Valor a ser pago R$ {valor:.2f}")
    
      