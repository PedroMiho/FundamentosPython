listaNotas = []

while True:
    notas = int(input("Digite suas notas: "))
    usuario = input("Deseja continuar [S/N] ?").upper()
    
    if usuario == "N":
        break
    else:
        listaNotas.append(notas)
        
        
        
maiorNota = max(listaNotas)
menorNota = min(listaNotas)
somaNotas = sum(listaNotas)        
mediaNotas = somaNotas/len(listaNotas)

print(f"A maior nota digitada {maiorNota}")
print(f"A menor nota digitada {menorNota}")
print(f"A soma das nota digitadas {somaNotas}")
print(f"A media das nota digitadas {mediaNotas}")