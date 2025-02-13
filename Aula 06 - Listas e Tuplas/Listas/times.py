listaTimes = ["Santos" , "Palmeiras" , "Corinthians", "São Paulo"]

#Adicionando item na ultima posição de uma lista 
listaTimes.append("Flamengo")
print(listaTimes)

#Adicionando item numa posição especifica
listaTimes.insert(1 , "Portuguesa")
print(listaTimes)

#Verificando o tamanho de uma lista
print(len(listaTimes))

#Remover um item da lista
listaTimes.remove("Palmeiras")
print(listaTimes)

#Pegando a posição de item na lista 
print(listaTimes.index("Corinthians"))

#Organizando em ordem alfabetica
print(sorted(listaTimes))