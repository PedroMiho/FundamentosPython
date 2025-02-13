# Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for impar desconsidere-o.

soma = 0 

for var in range (1,7):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        soma = soma + numero

print(soma)