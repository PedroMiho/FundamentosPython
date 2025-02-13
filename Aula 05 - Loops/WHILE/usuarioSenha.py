# Criar um codigo que verifique se o usuario acertou o login e senha, caso 
# não acerte, ele pode tentar novamente por mais 5 vezes.

loginSalvo = "pedromiho"
senhaSalva = "1234"
vezes = 1
while True:
    usuario = input("Digite seu usuario: ").lower()
    senha = input("Digite sua senha: ")
    
    if loginSalvo == usuario and senha == senhaSalva:
        print("Pode jogar clash")
        break
    elif vezes >= 5:
        print("Aguarde 1 minuto e tente novamente ")
        break
    else :
        print("Tente novamente")
        vezes += 1