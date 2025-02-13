n1 = int(input("Digite a nota do aluno: "))
n2 = int(input("Digite a nota do aluno: "))

media = (n1 + n2) / 2

if media >= 70:
    print("Aprovado")
    
elif media >= 50:
    print("Recuperação")
    
    n3 = int(input("Digite a nota da prova de recuperação: "))
    media = (media + n3) / 2
    
    if media >= 70:
        print("Aprovado")
    else:        
        print("Reprovado")       
         
else:
    print("Reprovado")
