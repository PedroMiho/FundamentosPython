#Exercicio 1: Login e Senha
loginSalvo = "pedromiho"
senhaSalva = "1234"

loginUser = input("Digite o seu login: ").lower()
senhaUser = input("Digite a sua senha: ")

if loginUser == loginSalvo and senhaUser == senhaSalva:
    print("Pode jogar, Clash Royale")
else:
    print("Login e Senha invalidos")
    

#Exercicio 2: Nota e frequência
nota = int(input("Digite a sua nota:"))
frequencia = int(input("Digite a sua frequencia:"))

notaMinima = 50
frequenciaMinima = 75

if nota < 40 or frequencia < frequenciaMinima:
    print("Volte ano que vem")
elif nota >= notaMinima and frequencia >= frequenciaMinima:
    print("Aprovado")
elif nota >= 40 and nota < 50: 
    print("Recuperação")