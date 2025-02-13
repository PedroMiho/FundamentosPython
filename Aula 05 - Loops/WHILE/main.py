#Estrutura de Repetição - For
#Utilizada quando o programador sabe o inicio e fim.

#Estrutura de Repetição - While
#Utilizada quando o programador nao sabe o inicio e fim.

# Crie um programa que some e tire a media de todos os valores que o usuario digitar

soma = 0
media = 0
vezes = 0
while True:
    numero = int(input("Digite um numero: "))
    usuario = input("Você quer continuar [S/N]: ").upper()
    
    soma = soma + numero
    vezes = vezes + 1
    
    if usuario == "N":
        break

print(f"A soma foi igual a {soma}")
print(f"A media foi igual a {soma/vezes}")

