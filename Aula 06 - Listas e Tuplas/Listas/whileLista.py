lista = []

while True:
    usuario = int(input("Digite um valor para adicionar na lista: "))
    if usuario == 999:
        break
    else:
        lista.append(usuario)
print(lista)


#Percorrendo uma lista:
for valor in lista:
    print(valor)