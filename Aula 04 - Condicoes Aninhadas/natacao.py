# A confederação Nacional de Natação precisa de uma programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo com a idade.
# 	Até 9 anos: MIRIM
# 	Até 14 anos: INFANTIL
# 	Até 19 anos: JUNIOR
# 	Até 24 anos: SÊNIOR
# 	Acima: MASTER

# # OPÇÃO 1 - Capturando a idade 
# idade = input("Digite a sua idade: ")

# OPÇÃO 2 - Capturando ano de nascimento 
import datetime

dataAtual = datetime.date.today()
anoAtual = dataAtual.year
mesAtual = dataAtual.month
diaAtual = dataAtual.day

anoNascimento = input("Digite o seu ano de nascimento: ")
idade = anoAtual - anoNascimento

if idade <= 9:
    print("MIRIM") 
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 24:
    print("SENIOR")
else:
    print("MASTER")
