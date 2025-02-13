# Faça um programa que calcule a soma entre todos os números
# ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
soma = 0
for var in range (1 , 501):
    impar = var % 2
    multiploTres = var % 3
    if impar == 1 and multiploTres == 0:
        print(var)
        soma = soma + var
print(soma)