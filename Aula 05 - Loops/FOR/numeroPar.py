#Verificar os numeros pares entre 0 ate 50
# for var in range (0,51):
#     if var % 2 == 0:
#         print(var)

#Verificando soma a media de 6 valores digitados
soma = 0
media = 0
for var in range (1 , 7):
    numero = int(input('Digite um numero: '))
    soma = soma + numero
    media = media + 1
    
mediaFinal = soma / media
print(soma)
print(mediaFinal)